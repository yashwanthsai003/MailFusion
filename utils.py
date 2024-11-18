# utils.py
from models import db, EmailData, EmailConfig, EmailStatus
from jinja2 import Template
from transformers import pipeline
import requests
import time

from celery_worker import celery
from flask_socketio import SocketIO, emit
from flask import current_app

# Initialize the language generation pipeline
text_generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

@celery.task
def send_emails_task():
    from app import socketio  # Import here to avoid circular import
    email_config = EmailConfig.query.first()
    email_data_list = EmailData.query.all()
    total_emails = len(email_data_list)
    emails_sent = 0
    throttle_rate = email_config.throttle_rate
    delay_between_emails = 60 / throttle_rate if throttle_rate > 0 else 0

    for email_data in email_data_list:
        prompt_template = Template(email_config.prompt)
        prompt = prompt_template.render(**email_data.data)
        try:
            generated_text = text_generator(prompt, max_length=500, do_sample=True)[0]['generated_text']
            email_content = generated_text
            # Send email via Mailgun
            response = send_email_via_mailgun(email_config, email_data.email, email_content)
            if response.status_code == 200:
                status = 'Sent'
            else:
                status = 'Failed'
            # Update status
            email_status = EmailStatus(
                recipient=email_data.email,
                status=status
            )
            db.session.add(email_status)
            db.session.commit()
            # Emit update
            socketio.emit('email_status', {'recipient': email_data.email, 'status': status}, namespace='/')
            emails_sent += 1
            progress = int((emails_sent / total_emails) * 100)
            socketio.emit('progress', {'progress': progress}, namespace='/')
            time.sleep(delay_between_emails)
        except Exception as e:
            # Handle exceptions and continue
            email_status = EmailStatus(
                recipient=email_data.email,
                status='Failed'
            )
            db.session.add(email_status)
            db.session.commit()
            socketio.emit('email_status', {'recipient': email_data.email, 'status': 'Failed'}, namespace='/')
            continue

def send_email_via_mailgun(email_config, recipient, content):
    MAILGUN_API_KEY = current_app.config['MAILGUN_API_KEY']
    MAILGUN_DOMAIN = current_app.config['MAILGUN_DOMAIN']
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": email_config.email_address,
            "to": recipient,
            "subject": "Personalized Email",
            "html": content,
            "o:tracking": "yes",
            "o:tracking-opens": "yes",
            "o:tracking-clicks": "yes",
        }
    )
# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

db = SQLAlchemy()

class EmailData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    data = db.Column(db.JSON, nullable=False)

    @staticmethod
    def process_csv(filepath):
        df = pd.read_csv(filepath)
        # Validate if 'Email' column exists
        if 'Email' not in df.columns:
            raise Exception("CSV file must contain 'Email' column.")
        db.session.query(EmailData).delete()
        for _, row in df.iterrows():
            email_data = EmailData(
                email=row['Email'],
                data=row.to_dict()
            )
            db.session.add(email_data)
        db.session.commit()

    @staticmethod
    def get_columns():
        first_entry = EmailData.query.first()
        if first_entry:
            return list(first_entry.data.keys())
        else:
            return []

class EmailConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, nullable=False)
    schedule_time = db.Column(db.DateTime, nullable=False)
    throttle_rate = db.Column(db.Integer, nullable=False)
    smtp_server = db.Column(db.String(120), nullable=False)
    smtp_port = db.Column(db.Integer, nullable=False)
    email_address = db.Column(db.String(120), nullable=False)
    email_password = db.Column(db.String(120), nullable=False)

    @staticmethod
    def save_config(form):
        db.session.query(EmailConfig).delete()
        email_config = EmailConfig(
            prompt=form.prompt.data,
            schedule_time=form.schedule_time.data,
            throttle_rate=form.throttle_rate.data,
            smtp_server=form.smtp_server.data,
            smtp_port=form.smtp_port.data,
            email_address=form.email_address.data,
            email_password=form.email_password.data
        )
        db.session.add(email_config)
        db.session.commit()

class EmailStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    delivery_status = db.Column(db.String(50), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
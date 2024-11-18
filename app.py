import os
from dotenv import load_dotenv
load_dotenv()  # Loading environment variables from .env
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db, EmailData, EmailConfig, EmailStatus
from forms import UploadForm, ConfigureForm
from celery_worker import make_celery
from utils import send_emails_task

# Initializing flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initializing extensions
db.init_app(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, message_queue=app.config['SOCKETIO_MESSAGE_QUEUE'])

# Initializing celery
celery = make_celery(app)

# Checking uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = file.filename
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        # Process CSV and store in database
        try:
            EmailData.process_csv(filepath)
            flash('File uploaded and processed successfully!', 'success')
            return redirect(url_for('configure'))
        except Exception as e:
            flash(f'Error processing file: {e}', 'danger')
    return render_template('index.html', form=form)

@app.route('/configure', methods=['GET', 'POST'])
def configure():
    form = ConfigureForm()
    # Dynamically populating placeholders based on uploaded CSV columns
    columns = EmailData.get_columns()
    form.prompt.description = 'Available placeholders: ' + ', '.join(['{' + col + '}' for col in columns])
    if form.validate_on_submit():
        # Saveing configuration to database
        try:
            EmailConfig.save_config(form)
            # Scheduling email sending task
            send_time = form.schedule_time.data
            send_emails_task.apply_async(eta=send_time)
            flash('Emails scheduled successfully!', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f'Error saving configuration: {e}', 'danger')
    return render_template('configure.html', form=form)

@app.route('/dashboard')
def dashboard():
    emails = EmailStatus.query.all()
    return render_template('dashboard.html', emails=emails)

# SocketIO event handlers
@socketio.on('connect')
def handle_connect():
    pass

if __name__ == '__main__':
    socketio.run(app, debug=True)
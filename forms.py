# forms.py
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField, IntegerField, DateTimeField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange

class UploadForm(FlaskForm):
    file = FileField('Upload CSV File', validators=[DataRequired()])
    submit = SubmitField('Upload')

class ConfigureForm(FlaskForm):
    prompt = TextAreaField('Email Prompt', validators=[DataRequired()], render_kw={"rows": 5})
    schedule_time = DateTimeField('Schedule Time', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    throttle_rate = IntegerField('Throttle Rate (emails per minute)', validators=[DataRequired(), NumberRange(min=1)])
    smtp_server = StringField('SMTP Server', validators=[DataRequired()])
    smtp_port = IntegerField('SMTP Port', validators=[DataRequired()])
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    email_password = PasswordField('Email Password', validators=[DataRequired()])
    submit = SubmitField('Configure and Schedule')
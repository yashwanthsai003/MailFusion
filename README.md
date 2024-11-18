---

# **MailFusion**

MailFusion is an application that sends customized emails, optimized to increase the efficiency and personalization of your email campaigns. MailFusion allows users to upload recipient lists in CVS format, customize email content with dynamic placeholders, personalize emails with the GPT-Neo-125M model, schedule emails along with throttling capability and check the campaign statistic with a live analytics dashboard.

---

## **Table of Contents**
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  1. [Clone the Repository](#1-clone-the-repository)
  2. [Navigate to Project Directory](#2-navigate-to-project-directory)
  3. [Set Up Virtual Environment](#3-set-up-virtual-environment)
  4. [Install Dependencies](#4-install-dependencies)
  5. [Configure Environment Variables](#5-configure-environment-variables)
  6. [Initialize the Database](#6-initialize-the-database)
  7. [Start Redis Server](#7-start-redis-server)
  8. [Start Celery Worker](#8-start-celery-worker)
  9. [Run the Application](#9-run-the-application)
- [Usage Instructions](#usage-instructions)
  1. [Upload Recipient Data](#1-upload-recipient-data)
  2. [Configure Email Settings](#2-configure-email-settings)
  3. [Monitor Email Campaign](#3-monitor-email-campaign)
- [Troubleshooting](#troubleshooting)
- [Acknowledgements](#acknowledgements)

---

## **Features**
- **CSV Upload**: Easily upload recipient data using CSV files.
- **Dynamic Email Content**: Customize emails with dynamic placeholders based on recipient data.
- **AI-Powered Personalization**: Utilize the GPT-Neo-125M model to generate personalized email content.
- **Scheduling & Throttling**: Schedule emails to be sent at specific times and control the rate of sending.
- **Real-Time Monitoring**: Track the status of your email campaigns through a dynamic dashboard with real-time updates.
- **Mailgun Integration**: Use Mailgun's API for reliable email delivery and tracking.

---

## **Prerequisites**
Before setting up the MailFusion application, ensure you have the following installed on your Windows machine:
- **Python 3.8 or Higher**: [Download Python](https://www.python.org/downloads/)
- **Redis Server**: [Download Redis for Windows](https://github.com/microsoftarchive/redis/releases)
- **Git**: [Download Git](https://git-scm.com/)
- **Visual Studio Code (VS Code)**: [Download VS Code](https://code.visualstudio.com/)
- **Mailgun Account (Optional)**: Required for sending emails via Mailgun. [Sign Up for Mailgun](https://www.mailgun.com/)
- **Internet Connection**: To download necessary packages and the GPT-Neo model.

---

## **Project Structure**
```
MailFusion/
│
├── app.py
├── models.py
├── forms.py
├── utils.py
├── celery_worker.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── configure.html
│   └── dashboard.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
└── uploads/
```

---

## **Setup Instructions**

### 1. **Clone the Repository**
If you haven't already cloned the repository, follow these steps:
- Open Command Prompt or PowerShell.
- Navigate to the directory where you want to clone the project:
  ```bash
  cd /path/to/your/desired/directory
  ```
- Clone the repository:
  ```bash
  git clone https://github.com/yashwanthsai003/MailFusion.git
  ```
- Navigate into the project directory:
  ```bash
  cd MailFusion
  ```

---

### 2. **Navigate to Project Directory**
Ensure you're in the project directory:
```bash
cd /path/to/your/desired/directory/MailFusion
```

---

### 3. **Set Up Virtual Environment**
Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 4. **Install Dependencies**
Install all necessary Python packages:
```bash
pip install -r requirements.txt
```

---

### 5. **Configure Environment Variables**
Create a `.env` file in the root directory and add the following:
```
SECRET_KEY=supersecretkey123
MAILGUN_API_KEY=your-mailgun-api-key
MAILGUN_DOMAIN=your-mailgun-domain
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
SOCKETIO_MESSAGE_QUEUE=redis://localhost:6379/0
```
Replace the placeholder values accordingly.

---

### 6. **Initialize the Database**
Set up the SQLite database:
```bash
flask db init
flask db migrate
flask db upgrade
```

---

### 7. **Start Redis Server**
Run the Redis server:
```bash
redis-server.exe
```

---

### 8. **Start Celery Worker**
Run Celery to handle background tasks:
```bash
celery -A celery_worker.celery worker --loglevel=info
```

---

### 9. **Run the Application**
Start the Flask development server:
```bash
flask run
```
Access the application at `http://localhost:5000`.

---

## **Usage Instructions**

### 1. **Upload Recipient Data**
- Upload a CSV file containing recipient details on the homepage.

### 2. **Configure Email Settings**
- Enter dynamic placeholders in the email template (e.g., `{FirstName}`).
- Schedule emails and set a throttle rate.

### 3. **Monitor Email Campaign**
- Track the progress and status of emails on the dashboard.

---

## **Troubleshooting**
Refer to the common troubleshooting steps in the original README for Redis, Celery, or Flask issues.

---

## **Acknowledgements**
- **Flask**: Web framework
- **Celery**: Task queue
- **Redis**: Message broker
- **Mailgun**: Email delivery
- **Bootstrap**: Styling
- **Jinja2**: Templating

---

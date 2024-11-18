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

### **Usage Instructions**

Follow these steps to use the MailFusion application effectively:

#### 1. **Upload Recipient Data**
- **Access the Application**: 
  Open your browser and navigate to [http://localhost:5000](http://localhost:5000).
  
- **Upload CSV File**:
  - On the homepage, locate the "Upload CSV" section.
  - Click **"Choose File"** and select your CSV file containing recipient data.
  
- **CSV Format Requirements**:
  - The file must have at least one column labeled `Email`.
  - You can include additional columns (e.g., `FirstName`, `Company`) for personalized email content.
  
- **Submit**:
  - Click the **"Upload"** button to process the file.
  - A success message will appear if the upload is successful, and the data will be stored in the database.

#### 2. **Configure Email Settings**
- **Navigate to the Configuration Page**:
  After uploading the CSV file, you'll be redirected to the **"Configuration"** page.

- **Customize the Email Prompt**:
  - Enter the email content in the provided text box.
  - Use placeholders for dynamic content based on CSV columns, such as `{FirstName}`, `{Company}`, or `{ProductName}`.
  - Example:
    ```
    Dear {FirstName},
    
    We’re excited to share our latest product, {ProductName}, with you. Get an exclusive offer today!

    Best regards,
    Your Company
    ```

- **Schedule Email Sending**:
  - Select the desired date and time for sending emails.
  - If no schedule is set, emails will be sent immediately.

- **Set Throttling Options**:
  - Specify the rate limit (e.g., "Send 50 emails per hour") to comply with email provider limits.

- **Provide SMTP/ESP Details**:
  - Enter the required details for email delivery:
    - **SMTP Server**: Your email provider's server (e.g., `smtp.mailgun.org`).
    - **SMTP Port**: Typically `587` for TLS or `465` for SSL.
    - **Sender Email Address**: The email address you’re sending from.
    - **Password/API Key**: The password or API key for the sender's account.
  - Note: If you're testing without an actual ESP, placeholder credentials can be used.

- **Submit Configuration**:
  - Click **"Configure and Schedule"** to save the settings and schedule emails.
  - A confirmation message will appear upon successful scheduling.

#### 3. **Monitor Email Campaign**
- **Access the Dashboard**:
  - After scheduling, you’ll be redirected to the **"Dashboard"** page.
  - Alternatively, navigate to [http://localhost:5000/dashboard](http://localhost:5000/dashboard).

- **View Campaign Status**:
  - The dashboard provides a real-time overview of the email campaign:
    - **Progress Bar**: Shows the percentage of emails sent.
    - **Email Table**: Lists each recipient’s status, including:
      - **Recipient Email**
      - **Email Sending Status** (`Sent`, `Failed`, or `Pending`)
      - **Delivery Status** (if tracked via Mailgun, e.g., `Delivered`, `Opened`, or `Bounced`)
      - **Timestamp** (when the email was processed)

- **Real-Time Updates**:
  - The table and progress bar update automatically as emails are processed.
  - Failed emails will display appropriate error messages in the table.

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

# MailFusion

**MailFusion** is an application that sends customized emails, optimized to increase the efficiency and personalization of your email campaigns. MailFusion allows users to upload recipient lists in CVS format, customize email content with dynamic placeholders, personalize emails with the GPT-Neo-125M model, schedule emails along with throttling capability and check the campaign statistic with a live analytics dashboard.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Navigate to Project Directory](#2-navigate-to-project-directory)
  - [3. Set Up Virtual Environment](#3-set-up-virtual-environment)
  - [4. Install Dependencies](#4-install-dependencies)
  - [5. Configure Environment Variables](#5-configure-environment-variables)
  - [6. Initialize the Database](#6-initialize-the-database)
  - [7. Start Redis Server](#7-start-redis-server)
  - [8. Start Celery Worker](#8-start-celery-worker)
  - [9. Run the Application](#9-run-the-application)
- [Usage Instructions](#usage-instructions)
  - [1. Upload Recipient Data](#1-upload-recipient-data)
  - [2. Configure Email Settings](#2-configure-email-settings)
  - [3. Monitor Email Campaign](#3-monitor-email-campaign)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **CSV Upload:** Easily upload recipient data using CSV files.
- **Dynamic Email Content:** Customize emails with dynamic placeholders based on recipient data.
- **AI-Powered Personalization:** Utilize the GPT-Neo-125M model to generate personalized email content.
- **Scheduling & Throttling:** Schedule emails to be sent at specific times and control the rate of sending to comply with best practices.
- **Real-Time Monitoring:** Track the status of your email campaigns through a dynamic dashboard with real-time updates.
- **Mailgun Integration:** Use Mailgun's API for reliable email delivery and tracking.

## Prerequisites

Before setting up the MailFusion application, ensure you have the following installed on your Windows machine:

- **Python 3.8 or Higher:** [Download Python](https://www.python.org/downloads/windows/)
- **Redis Server:** [Download Redis for Windows](https://github.com/microsoftarchive/redis/releases)
- **Git:** [Download Git](https://git-scm.com/download/win)
- **Visual Studio Code (VS Code):** [Download VS Code](https://code.visualstudio.com/download)
- **Mailgun Account (Optional):** Required for sending emails via Mailgun. [Sign Up for Mailgun](https://www.mailgun.com/)
- **Internet Connection:** To download necessary packages and the GPT-Neo model.

## Project Structure

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

## Setup Instructions

Follow these steps to set up and run the MailFusion application on your Windows machine.

### 1. Clone the Repository

If you haven't already cloned the repository, follow these steps. If you've already done this, you can skip to the next step.

1. **Open GitHub Repository:**

   - Navigate to your GitHub repository: [MailFusion Repository](https://github.com/yashwanthsai003/MailFusion)

2. **Clone the Repository:**

   - Open **Command Prompt** or **PowerShell**.
   - Navigate to the directory where you want to clone the project:
     ```bash
     cd C:\Users\yashw\OneDrive\Documents
     ```
   - Clone the repository:
     ```bash
     git clone https://github.com/yashwanthsai003/MailFusion.git
     ```
   - Navigate into the project directory:
     ```bash
     cd MailFusion
     ```

### 2. Navigate to Project Directory

If you've already cloned the repository, ensure you're in the project directory.

```bash
cd C:\Users\yashw\OneDrive\Documents\MailFusion
```

### 3. Set Up Virtual Environment

Creating a virtual environment ensures that your project dependencies are isolated from other Python projects.

1. **Create Virtual Environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment:**

   ```bash
   venv\Scripts\activate
   ```

   - After activation, your command prompt should show `(venv)` at the beginning.

### 4. Install Dependencies

Install all necessary Python packages using `pip` and the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Environment variables are used to store sensitive information securely.

1. **Create a `.env` File:**

   - In the root directory (`MailFusion`), create a new file named `.env`.

2. **Add the Following Content to `.env`:**

   ```plaintext
   SECRET_KEY=your-secret-key
   MAILGUN_API_KEY=your-mailgun-api-key
   MAILGUN_DOMAIN=your-mailgun-domain
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   SOCKETIO_MESSAGE_QUEUE=redis://localhost:6379/0
   ```

   - **Replace Placeholder Values:**
     - `your-secret-key`: Generate a random string. For example, `supersecretkey123`.
     - `your-mailgun-api-key`: Your Mailgun API key. If you don't have one, leave it as a placeholder.
     - `your-mailgun-domain`: Your Mailgun domain (e.g., `sandbox12345.mailgun.org`). If you don't have one, leave it as a placeholder.

   **Example:**

   ```plaintext
   SECRET_KEY=supersecretkey123
   MAILGUN_API_KEY=key-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   MAILGUN_DOMAIN=sandboxxxxxxxxxxxxxxxxxxxxxxxxx.mailgun.org
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   SOCKETIO_MESSAGE_QUEUE=redis://localhost:6379/0
   ```

   **Note:** Without valid Mailgun credentials, the email-sending functionality will not work. However, the rest of the application will function as expected.

### 6. Initialize the Database

Set up the SQLite database and apply migrations.

1. **Initialize Migrations:**

   ```bash
   flask db init
   ```

2. **Create Migration Scripts:**

   ```bash
   flask db migrate
   ```

3. **Apply Migrations:**

   ```bash
   flask db upgrade
   ```

### 7. Start Redis Server

Celery uses Redis as a message broker. Ensure Redis is running.

1. **Open Command Prompt:**

   - Press **Win + R**, type `cmd`, and press **Enter**.

2. **Navigate to Redis Installation Directory:**

   - Replace the path below with the actual path where Redis is installed.
   - **Example:**
     ```bash
     cd "C:\Program Files\Redis"
     ```

3. **Start Redis Server:**

   ```bash
   redis-server.exe
   ```

   - A new window should open, indicating that Redis is running.

### 8. Start Celery Worker

Celery handles background tasks like sending emails.

1. **Open a New Command Prompt Window:**

   - Keep the Redis server running in its window.

2. **Navigate to Project Directory and Activate Virtual Environment:**

   ```bash
   cd C:\Users\yashw\OneDrive\Documents\MailFusion
   venv\Scripts\activate
   ```

3. **Start Celery Worker:**

   ```bash
   celery -A celery_worker.celery worker --loglevel=info
   ```

   - This will start the Celery worker, which listens for tasks to execute.

### 9. Run the Application

Start the Flask development server.

1. **Open Another Command Prompt Window:**

   - Keep both Redis and Celery running in their respective windows.

2. **Navigate to Project Directory and Activate Virtual Environment:**

   ```bash
   cd C:\Users\yashw\OneDrive\Documents\MailFusion
   venv\Scripts\activate
   ```

3. **Run the Flask Application:**

   ```bash
   flask run
   ```

   - The application will start and be accessible at `http://localhost:5000`.

## Usage Instructions

Follow these steps to use the MailFusion application.

### 1. Upload Recipient Data

1. **Access the Application:**

   - Open your web browser and navigate to `http://localhost:5000`.

2. **Upload CSV File:**

   - On the homepage, you'll see a form to upload a CSV file.
   - Click on **"Choose File"** and select your CSV file containing recipient data.
   - **CSV Format Requirements:**
     - The CSV file **must** contain an `Email` column.
     - Additional columns can be used as placeholders in the email content.
   - Click **"Upload"** to submit the file.

3. **Processing:**

   - After uploading, the application will process the CSV file and store recipient data in the database.
   - You'll receive a success message upon successful processing.

### 2. Configure Email Settings

1. **Navigate to Configuration:**

   - After uploading the CSV, you'll be redirected to the configuration page.

2. **Customize Email Prompt:**

   - Enter the email prompt in the provided textarea.
   - Use dynamic placeholders based on the CSV columns. For example:
     ```
     Dear {FirstName},

     We are excited to offer you a special discount on our new product...

     Best regards,
     Your Company
     ```

3. **Schedule Email Sending Time:**

   - Select the date and time when you want the emails to be sent.

4. **Set Throttle Rate:**

   - Define the number of emails to be sent per minute to comply with best practices and avoid being marked as spam.

5. **SMTP/ESP Settings:**

   - **SMTP Server:** Your email service provider's SMTP server (e.g., `smtp.mailgun.org`).
   - **SMTP Port:** Typically `587` for TLS or `465` for SSL.
   - **Email Address:** The sender's email address.
   - **Email Password:** The password or API key for the sender's email account.

   **Note:** Since you don't have actual Mailgun credentials, you can leave these fields as placeholders.

6. **Submit Configuration:**

   - Click **"Configure and Schedule"** to save settings and schedule the email-sending task.
   - You'll receive a success message upon successful scheduling.

### 3. Monitor Email Campaign

1. **Access the Dashboard:**

   - After scheduling, you'll be redirected to the dashboard page.
   - Alternatively, navigate to `http://localhost:5000/dashboard`.

2. **View Progress:**

   - A progress bar will indicate the percentage of emails sent.
   - A table will display the status of each email, including:
     - **Recipient:** The email address of the recipient.
     - **Status:** Indicates whether the email was sent successfully or failed.
     - **Delivery Status:** Shows delivery confirmations if available.
     - **Timestamp:** The time when the email was sent.

   **Note:** Without valid Mailgun credentials, the delivery status will not be available, and email sending will not function.

## Troubleshooting

Here are some common issues and how to resolve them:

### 1. **Redis Server Not Starting**

- **Issue:** Unable to start Redis server.
- **Solution:**
  - Ensure you've downloaded the correct version of Redis for Windows.
  - Run the Command Prompt as an administrator.
  - Check if another application is using port `6379`. If so, stop that application or configure Redis to use a different port.

### 2. **Celery Worker Not Starting**

- **Issue:** Celery worker fails to start or connect to Redis.
- **Solution:**
  - Ensure Redis server is running.
  - Verify that `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` in your `.env` file are correctly set to `redis://localhost:6379/0`.
  - Activate the virtual environment before starting the Celery worker.

### 3. **Flask Application Not Running**

- **Issue:** Unable to start Flask server.
- **Solution:**
  - Ensure the virtual environment is activated.
  - Check for syntax errors in your code files.
  - Verify that all dependencies are installed (`pip install -r requirements.txt`).

### 4. **Emails Not Sending**

- **Issue:** Emails are not being sent.
- **Solution:**
  - Ensure that `MAILGUN_API_KEY` and `MAILGUN_DOMAIN` in your `.env` file are correctly set.
  - Verify that your Mailgun account is active and the domain is verified.
  - Check Celery worker logs for any error messages related to email sending.

### 5. **Real-Time Updates Not Working**

- **Issue:** Dashboard not updating in real-time.
- **Solution:**
  - Ensure that Flask-SocketIO is correctly configured.
  - Verify that the Socket.IO client library is included in your templates.
  - Check for any JavaScript errors in the browser console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Celery](https://docs.celeryproject.org/)
- [Redis](https://redis.io/)
- [Mailgun](https://www.mailgun.com/)
- [Transformers by Hugging Face](https://huggingface.co/transformers/)
- [Bootstrap](https://getbootstrap.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
```


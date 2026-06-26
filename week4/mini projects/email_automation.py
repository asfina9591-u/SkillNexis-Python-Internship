# Automate Email Sending with smtplib
import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_app_password"  # Use Gmail App Password

msg = MIMEText("Hello, this is an automated email from Python!")
msg["Subject"] = "Test Email"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email sent successfully!")

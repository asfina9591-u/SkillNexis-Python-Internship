import csv
import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "asfina9591@gmail.com"
APP_PASSWORD = "ymksoecinoeeyhci"   # not your real password

def send_email(to_email, subject, message):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

def main():
    with open("students.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Name"]
            email = row["Email"]
            subject = f"Hello {name}, important update!"
            message = f"Hi {name},\n\nThis is an automated message just for you.\n\nBest,\nAsfina"
            send_email(email, subject, message)
            print(f"Email sent to {name} ({email})")

if __name__ == "__main__":
    main()
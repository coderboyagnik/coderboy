import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "your_email@gmail.com"
    password = "your_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

if __name__ == "__main__":
    subject = input("Enter the subject: ")
    body = input("Enter the body: ")
    to_email = input("Enter the recipient email: ")
    send_email(subject, body, to_email)

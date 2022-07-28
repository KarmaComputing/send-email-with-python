import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

MAIL_FROM = os.getenv("MAIL_FROM", "noreply@example.com")
MAIL_TO = os.getenv("MAIL_TO", "bob@example.com")
SMTP_HOST = os.getenv("SMTP_HOST", "email.example.com")
SMTP_PASSWORD os.getenv("SMTP_PASSWORD", "secret")

smtp_server = SMTP_HOST
port = 25
sender = MAIL_FROM
password = SMTP_PASSWORD

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender
message["To"] = MAIL_TO
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

text = message.as_string()

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, MAIL_TO, message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()

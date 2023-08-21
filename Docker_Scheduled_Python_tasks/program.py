import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

smtp_port = 
smtp_server = 
sender_mail = "pashatempmarket@gmail.com"
sender_pw = "12345"
receipients = "pavel.fankouski@gmail.com"

def send_alert(title, message):
    message = MIMEMultipart("alternative")
    message["subject"] = f'{title}'
    message["from"] = sender_mail
    message["To"] = ", ".join(receipients)
    body = f"{message}"
    message.attach(MIMEText(body,"html"))
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_port, smtp_server) as server:
        server.starttls(context=context)
        server.login(sender_mail, sender_pw)
        server.sendmail(sender_mail, receipients, message.as_string())

if __name__ == "__main__":
    print(f"Running script at {datetime.now()}")
    send_alert("This message is send every 17 minutes", "<h1>Hello World from Docker container</h1>")
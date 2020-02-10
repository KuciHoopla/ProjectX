import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import *
from email.mime.text import MIMEText


def send_mail(path_pdf, email, number):
    subject = f"Invoice nr: {number} from Energy Kft."
    body = "Dear customer, \n please find invoice in attachment."
    sender_email = "invoice.rpa.2020@gmail.com"
    receiver_email = email
    password = "Automationproject2020"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    filename = path_pdf

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= invoice.pdf",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)



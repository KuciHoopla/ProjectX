import smtplib
import ssl
from email.mime.multipart import *
from email.mime.text import MIMEText

from creators.database.database_reporter import insert_report


def open_server():
    # sender_email = "invoice.rpa.2020@gmail.com"
    sender_email = "rpa.automation2020@gmail.com"
    password = "Automationproject2020"
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(sender_email, password)
    insert_report(passed="server connected")
    return server


def send_mail(path_pdf, email, number):
    subject = f"Invoice nr: {number} from Energy Kft."
    body = "Dear customer, \n please find invoice in attachment."
    sender_email = "invoice.rpa.2020@gmail.com"
    receiver_email = email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    filename = path_pdf
    file = open(filename, errors='ignore')
    # Open PDF file in binary mode
    part = MIMEMultipart()
    part.attach(MIMEText(file.read()))

# Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= invoice.pdf",
    )

# Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

# Log in to server using secure context and send email

    return text
    # server.sendmail(sender_email, receiver_email, text)



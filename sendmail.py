import logging
import smtplib
from email.message import EmailMessage
from decouple import config


def send(subject, recipient, body):
    email_server = config('EMAIL_SERVER', 'smtp.gmail.com')
    email_server_port = config('EMAIL_SERVER_PORT', 465)
    email_user = config('EMAIL_USER')
    email_password = config('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = subject
    msg['From'] = email_user
    msg['To'] = recipient

    logger.info('\nSendmail: Attempting to send email.. (Server={}, Port={}, User={}, To={})\n'.format(email_server, email_server_port, email_user, recipient))
    
    if email_server and email_server_port and email_user and email_password and recipient:
        server = smtplib.SMTP_SSL(email_server, email_server_port)
        server.set_debuglevel(1)
        server.ehlo()
        server.login(email_user, email_password)
        server.send_message(msg)
        server.close()
        logger.info('\nSendmail: Sent email to: {}\n'.format(recipient))

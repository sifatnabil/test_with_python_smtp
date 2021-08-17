import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL_ADDRESS")
sender_pass = os.getenv("EMAIL_PASS")

msg = EmailMessage()
msg['Subject'] = 'This is a test message.'
msg['From'] = sender_email
msg['To'] = 'sifatnabil@gmail.com'
msg.set_content('A test message from python')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
    smtp.login(sender_email, sender_pass)

    smtp.send_message(msg)


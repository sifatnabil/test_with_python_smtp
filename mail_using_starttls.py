import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL_ADDRESS")
sender_pass = os.getenv("EMAIL_PASS")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, sender_pass)

    subject = 'This is a test message.'
    body = 'A test message from python'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(sender_email, 'sifatnabil@gmail.com', msg)


import smtplib
import os
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL_ADDRESS")
sender_pass = os.getenv("EMAIL_PASS")

msg = EmailMessage()
msg['Subject'] = 'Sending some random images'
msg['From'] = sender_email
msg['To'] = 'sifatnabil@gmail.com'
msg.set_content(f'A test message containing multiple images')

msg.add_alternative('''
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is an HTML Email! </h1>
        </body>
    </html>
''', subtype="html")

files = ['random_image_1.jpg', 'random_image_2.jpg', 'random_image_3.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
    smtp.login(sender_email, sender_pass)
    smtp.send_message(msg)


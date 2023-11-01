import cases
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import imaplib
import os

def send_email(recipient: list[str], text: str, title: str, file: str = None,):
    SERVER = cases.smtp_server
    PASSWORD = cases.token
    USER = cases.mail

    msg = MIMEMultipart('alterrnative')
    msg['Subject'] = text
    msg['From'] = f'<Dz 13 {USER}>'
    msg['To'] =  ' '.join(recipient)
    msg['Reply_to'] = USER
    msg['Return_path'] = USER
    msg['x_mailer'] = 'decorator'

    if file:
        file_is = os.path.exists(file)
        if not file_is:
            print('to ne to')
        else:
            base_name = os.path.basename(file)
            file_size = os.path.getsize(file)
            second_file = MIMEBase('application', f'octet-stream; name = {base_name}')
            second_file.set_payload(open(file, 'rb').read())
            second_file.add_header('Content-Description', file)
            second_file.add_header('Content-Description', f'file; filename = {file}; size = {file_size}')
            encoders.encode_base64(second_file)
            msg.attach(second_file)




    text_send = MIMEText(text, 'plain')
    msg.attach(text_send)

    mail = smtplib.SMTP_SSL(SERVER)
    mail.login(USER, PASSWORD)
    mail.sendmail(USER,recipient, msg.as_string())
    mail.quit()





def checking_email():
    PASSWORD = cases.token
    USER = cases.mail
    SERVER = cases.imap_server
    imap = imaplib.IMAP4_SSL(SERVER)
    logged_in = imap.login(USER, PASSWORD)
    # print(logged_in)
    # print(logged_in[1] [-1].decode())
    print(imap.select('INBOX'))
    print(imap.search(None, ''))
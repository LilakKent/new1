import smtplib
from hilel_praktice.emails.emails import gmail

def send_email(message):
    sender = gmail['email']
    password = gmail['password']

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)

        return "The message was sent!"
    except Exception as _ex:
        return f'{_ex}\nCheck ur login or password pls'

def main():
    message = input('type ur mail')
    print(send_email(message=message))

if __name__ == '__main__':
    main()
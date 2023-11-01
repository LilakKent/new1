from hilel_praktice.emails.emails import emails_hilel
from hilel_praktice.emails import cases


def main():
    recipient = [cases.mail]#shulika20@ukr.net
    text = 'Checking email'
    title = 'Hi'
    file = '../dz13.py'
    emails_hilel.send_email(recipient, text, title)
    emails_hilel.checking_email()


if __name__ == '__main__':
    main()
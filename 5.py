import smtplib

# Підключення до SMTP-сервера
smtp_server = 'smtp.example.com'
port = 587
username = 'your_username'
password = 'your_password'

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(username, password)

# Відправка листа
from_addr = 'your_email@example.com'
to_addrs = ['recipient1@example.com', 'recipient2@example.com']
message = 'Це тестове повідомлення.'

server.sendmail(from_addr, to_addrs, message)

# Закриття з'єднання
server.quit()

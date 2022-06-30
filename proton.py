import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("The body of the email")
msg["Subject"] = "Test1"
msg["From"] = "swypper1@proton.me"
msg["To"] = "test01235@bk.ru"

context=ssl.create_default_context()

try:
    smtp = smtplib.SMTP("mail.protonmail.com", 993)
    #127.0.0.1 1025
    smtp.set_debuglevel(True)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(msg["From"], "qGTgZ3qm")
    smtp.send_message(msg)
    smtp.close()
    print('OK')

except Exception as e:
    print(e)

# protontest1@yttest.xyz

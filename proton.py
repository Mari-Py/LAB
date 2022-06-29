import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("The body of the email")
msg["Subject"] = "Test1"
msg["From"] = "swypper1@proton.me"
msg["To"] = "beretta07@bk.ru"

context=ssl.create_default_context()

with smtplib.SMTP("127.0.0.1", port=1025) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], "qGTgZ3qm")
    smtp.send_message(msg)
    server.quit()

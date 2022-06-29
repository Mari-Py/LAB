import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("The body of the email")
msg["Subject"] = "Test1"
msg["From"] = "test01235@bk.ru"
msg["To"] = "beretta07@bk.ru"

context=ssl.create_default_context()

with smtplib.SMTP("smtp.mail.ru", port=587) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], "WiIY2OcQSjQ6komBrLNs")
    smtp.send_message(msg)

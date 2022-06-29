import smtplib

def send_email(subject, body_text, emails):

    from_addr = "test01235@bk.ru"

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % ', '.join(emails),
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP("smtp.mail.ru", 465)
    server.login('test01235@bk.ru', '135642!Sm')
    server.sendmail(from_addr, emails, BODY)
    server.quit()


if __name__ == "__main__":
    emails = ["beretta07@bk.ru"]
    subject = "test1"
    body_text = "123"
    send_email(subject, body_text, emails)
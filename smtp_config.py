import smtplib

def send_email(subject, body_text, emails):

    from_addr = "_"

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % ', '.join(emails),
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP("smtp.mail.ru", 465)
    server.login('_', '_')
    server.sendmail(from_addr, emails, BODY)
    server.quit()


if __name__ == "__main__":
    emails = ["_"]
    subject = "test1"
    body_text = "123"
    send_email(subject, body_text, emails)

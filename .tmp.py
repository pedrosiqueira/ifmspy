import smtplib
from email.mime.text import MIMEText


def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, headers=None):
    headers = headers if headers else {}

    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email["To"]
        email["To"] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()


send_email("A Party", "Friends and family only: a party", "me@example.com", "friend1@example.com", "family1@example.com", headers={"Reply-To": "me2@example.com"})

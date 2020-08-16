import smtplib as smtp
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

timeout = 1200
spacing = ' '
port = 587
smtp_server = "smtp.gmail.com"
server = smtp.SMTP(smtp_server, port, timeout=timeout)
msg = EmailMessage()


def get_recepient(to_address):
    if "gmail.com" not in to_address:
        print("Please enter an email from your email provider")
    else:
        return to_address


def get_smtp(server, email, password):
    context = ssl.create_default_context()
    server.starttls(context=context)
    try:
        server.login(email, password)
    except Exception as e:
        print("Username or password was wrong")
        print(e)


def check_message_length(message):
    if len(message) > 200:
        print("Only allowed a max of 200 characters")


def format_email(subject, email, to_address):
    msg = EmailMessage()
    mime = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to_address
    return mime


def format_body(message):
    part1 = MIMEText(message, 'plain')
    return part1


def main():
    on_menu = True
    while on_menu:
        print("Email Automation")
        print("Send Email")
        char = input("Hit [S] to send an email:").strip(spacing)
        if char.startswith('s') or char.startswith('S'):
            on_menu = False
    server = smtp.SMTP(smtp_server, port, timeout=timeout)
    email = input("Enter Email:")
    password = input("Enter password:")
    get_smtp(server, email, password)
    to_address = input("Enter address you want to send an email to:").strip(spacing)
    get_recepient(to_address)
    subject = input("Enter Subject of your email:")
    message = input("Ok final step enter your message(max. 1500 characters long)").strip(spacing)
    check_message_length(message)
    yes = "yes"
    character = ["Y", "y", yes.upper()]
    print(f"Email Review:\n{format_email(msg, subject, email)} Message:{format_body(message)}")
    msg.attach(message)
    confirmation = input("Is this correct?")
    if confirmation not in character:
        revised_message = input("Renter message:")
        check_message_length(revised_message)
    try:
        server.sendmail(email, to_address, msg.as_string())
        print("Email sent successfuly")
    except Exception:
        print(
            "Email could not be sent please check that you have an internet connection,your credentials are correct\nand you have given other apps permission to use your email account")


server.quit()

if __name__ == '__main__':
    main()

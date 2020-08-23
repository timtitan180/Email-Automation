# Currently this only works if the sender and recepient have a Gmail account. Sorry!
# I will make sure to make it acessible for more email providers in the upcoming versions.
# Thank you!

import smtplib as smtp
import ssl
from email.message import EmailMessage

timeout = 1200
spacing = ' '
port = 587
smtp_server = "smtp.gmail.com"
server = smtp.SMTP(smtp_server, port, timeout=timeout)

msg = EmailMessage()  # initializing EmailMessage class from email.message module to format email


def get_recepient(to_address):
    if "gmail.com" not in to_address:  # checking to make sure the email will be sent to a Gmail account
        print("Please enter an email from your email provider")
    else:
        return to_address


def get_smtp(server, email, password):
    context = ssl.create_default_context()  # using SSL to securely send the email
    server.starttls(context=context)
    try:
        server.login(email, password)
    except Exception as e:
        print("Username or password was wrong")
        print(e)
        retry_email = input("Enter email again:")
        retry_password = input("Enter password again")
        server.login(retry_email, retry_password)


def check_message_length(message):
    if len(message) > 20538:
        print("Only allowed a max of 20538 characters")


def format_subject(subject):
    msg['Subject'] = subject  # Subject: subject
    return subject


def format_recepient(to_address):
    msg['To'] = to_address  # To: to_addresss
    return to_address


def format_body(message):
    msg.set_content(message)  # message: message body
    return message


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

    message = input("Ok final step enter your message(max. 20538 characters allowed)").strip(spacing)

    check_message_length(message)

    yes = "yes"

    character = ["Y", "y", yes.upper()]
    print(
        f"Email Review:\nSubject:{format_subject(subject)}\nTo:{format_recepient(to_address)}\nMessage:{format_body(message)}")
    confirmation = input("Is this correct?")

    if confirmation not in character:
        revised_message = input("Renter message:")

        check_message_length(revised_message)
    try:
        server.sendmail(email, to_address,
                        msg.as_string())  # if everything is good the email will be sent if not an error will show

        print("Email sent successfuly")

    except Exception as e:
        print(e)


server.quit()

if __name__ == '__main__':
    main()

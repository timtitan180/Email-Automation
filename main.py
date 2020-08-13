import smtplib as smtp
import ssl

timeout = 1200
port = 587
smtp_server = "smtp.gmail.com"
server = smtp.SMTP(smtp_server, port, timeout=timeout)


def get_recepient(to_address):
    if "gmail.com" not in to_address:
        print("Please enter an email from your email provider")
    else:
        try:
            print("Success")
        except Exception as e:
            print(e)


def get_smtp(server, username, password):
    context = ssl.create_default_context()
    server.starttls(context=context)
    try:
        server.login(username, password)
    except Exception as e:
        print(e)


def check_message_length(message):
    if len(message) > 100:
        print("Only allowed a max of 100 characters")


def main():
    on_menu = True
    while on_menu:
        print("Email Automation")
        print("Send Email")
        char = input("Hit [S] to send an email:").strip()
        if char.startswith('s') or char.startswith('S'):
            on_menu = False
    username = input("Enter Email:")
    password = input("Enter password:")
    server = smtp.SMTP(smtp_server, port, timeout=timeout)
    get_smtp(server, username, password)
    to_address = input("Enter address you want to send an email to:").strip(' ')
    get_recepient(to_address)
    message = input("Ok final step enter your message(max of 1500 characters):").strip(' ')
    check_message_length(message)
    print("Successfuly sent!")
    with open("messages.txt", "w+") as file:
        file.write(message)
        file.close()


server.quit()


if __name__ == '__main__':
    main()
##
# yes = "yes"
# character = ["Y", "y", yes.upper()]
# print("So you want to send an email to" + to_address + "with the message:\n" + str(read_email))
# confirmation = input("Hit Y for if this is correct")
#
# if confirmation not in character:
#     revised_message = input("Renter message:")
#     check_message_length(revised_message)
#     option = input("Would you like to send another email?")
#     if not option.startswith("y"):
#         print("Thank you for choosing this application")
# server.quit()

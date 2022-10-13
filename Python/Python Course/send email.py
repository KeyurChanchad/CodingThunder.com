import smtplib


def send_email():
    to_add = "keyurchanchad21@gmail.com"
    from_add = "chanchadkeyur@gmail.com"
    user = "chanchadkeyur@gmail.com"
    password = "keyur21112001"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(from_add, to_add, content)
    server.quit()


if __name__ == '__main__':
    print("Starting a program file...")
    to = 'chanchadkeyur@gmail.com'
    content = "Keyur is a good boy. I am first time send email by a program in python."
    try:
        print("Email Sending.....")
        send_email()
        print("Done.. Email has been sent!.")

    except Exception as e:
        print("Sir, email is not sent....")


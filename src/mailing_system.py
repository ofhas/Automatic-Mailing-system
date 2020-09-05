import smtplib
import ssl
import datetime
import time


# using now() to get current time
while True:

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "sender_email@sender_email.com" # change to the address you wish to send from
    password = input("Type your password and press enter:")

    while True:

        a = datetime.datetime.now()
        eight_am = '08:00:00'
        current_date = a.strftime("%a, %b %d, %Y")
        array = ['testemail@testemail.com']  # add more contacts
        e = datetime.datetime.now()  # getting the time and current day of the week
        timestamp = time.strftime('%H:%M:%S')  # getting a 24 hour time format
        message = f"""\
Subject: Hi there today's date is - {current_date}

Write whatever mail content you wish....."""

       # this will limit the days you wish to send the mail, in our case the mail will be send from Sun - Thu
        if e.strftime("%a") == 'Sun' or e.strftime("%a") == 'Mon' or e.strftime("%a") == 'Tue' or e.strftime("%a") == 'Wed' or e.strftime("%a") == 'Thu':
            # you could also change the time the mail will be send
            if timestamp == eight_am:  # change to 08:00 AM
                for name in array:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()  # Can be omitted
                        server.starttls(context=context)
                        server.ehlo()  # Can be omitted
                        server.login(sender_email, password)
                        server.sendmail(sender_email, name, message)
                        print('Mail sent to:', name)

#!/usr/bin/env python
"""Alta3 Research | RZFeeser@alta3.com
   Sending an SMTP (email) with Python

   To run a development server, run
   
   python3 -m smtpd -c DebuggingServer -n localhost:1025

   in a seperate tmux window before running this script."""


import smtplib
from email.mime.text import MIMEText


def main():
    # this is routing information
    sender = 'HanSolo@example.com'
    receivers = ['Chewbacca@example.com']
    port = 1025

    # this is information appearing in the BODY of the email
    msg = MIMEText('The hyperdrive is less hyper and more drive. Can you check it out? Thanks.')

    msg['Subject'] = 'Hyperdrive is busted'
    # If the "From" and the "To" in the BODY do not match the routing information
    # your message will likely be hyperdrived into the trash by spam filters
    msg['From'] = 'HanSolo@example.com'
    msg['To'] = 'Chewbacca@example.com'

    # "localhost" would be replaced with something like "mail.gmail.com"
    # if we wanted to use an external server
    with smtplib.SMTP('localhost', port) as server:

        # server.login('username', 'password')  # this would be credentials to authenticate with the enterprise server
        # send the message
        server.sendmail(sender, receivers, msg.as_string())

    # announce locally that the message was sent
    print("Email has been sent.")

if __name__ == "__main__":
    main()


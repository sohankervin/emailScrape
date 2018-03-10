#! /usr/bin/python
"""
the purpose of this program is to scrape my email account and find key phrases within my email.
"""
# setting up the rudimentary bits to send email via Python.
import smtplib, imapclient, pyzmail, pprint
myPassword = raw_input("Please do not save your password in the source code, please enter it instead: ")

def connect() : 

    # utiilze port no. 587 because this is SMTP server Google resides on.
    emailObject = smtplib.SMTP('smtp.gmail.com', 587)
    # it's important to always initiate a connection to the server and greets the SMTP email server.
    emailObject.ehlo()
    # this sets up the encryption standard, and you can skip this with port 465 because the standard is already set up.
    emailObject.starttls()
    emailObject.login('sohankervin@gmail.com', myPassword)

    # this closes the connection 
    emailObject.quit()

def fetch_email() :
    # the following logs into IMAP server, which allows users to search for emails, fetch and extract text.
    coffee = imapclient.IMAPClient('imap.gmail.com', ssl = True)
    coffee.login('sohankervin@gmail.com', myPassword)

    # this will print out the list of folders you have available in a tuple format.
    pprint.pprint(coffee.list_folders())

    # read only is set to true so you don't delete emails unless you want to, in which you would set it to False.
    coffee.select_folder('INBOX', readonly= True)
    # this will return the UIDs for email, in this case the integer values
    UIDs = coffee.search(['FROM', 'contact@em2.nordstrom.com'])
    print UIDs

    # this will allow me to fetch my emails from a specific folder utilizing the UID returned from the previous function.
    creamer = coffee.fetch(UIDs, ['BODY[]'])
    emailMessage = pyzmail.PyzMessage.factory(creamer[28400 ]['BODY[]'])


    pprint.pprint(creamer)


    emailMessage.get_subject()
    emailMessage.get_addresses('from')
    emailMessage.text_part != None

    coffee.logout()
    # this closes the connection 

connect()
fetch_email()


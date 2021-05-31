#! python3
# textMyself.py - Defines the textmyself() finction that texts a message
# passed to it as a string.

# import needed module
from twilio.rest import Client
# Preset values:
accountSID = 'AC58188c049628a3c82cf429a05558bd83'
authToken = "b4d4195cf24d9ab9b0a83d663ac8975a"
twilioNumber1 = '+12166090979'
myNumber1 = '+886921965321'
myNumber2 = '+886936562182'

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber1, to=myNumber1)
    # twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber2)

# todo If you want to use the textmyself() function, just put textMyself.py to the same directory of your code
'''
import textmyself
textmyself.textmyself("The message to send to my phone.)
'''

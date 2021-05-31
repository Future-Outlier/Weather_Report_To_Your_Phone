#! python3
# textMyself.py - Defines the textmyself() finction that texts a message
# passed to it as a string.

# import needed module
from twilio.rest import Client
# Preset values:
accountSID = 'twilioaccountSID'
authToken = "twilioaccountSID"
twilioNumber1 = 'twilioNumber1'
myNumber1 = 'myNumber1'

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber1, to=myNumber1)
    # twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber2)

# todo If you want to use the textmyself() function, just put textMyself.py to the same directory of your code
'''
import textmyself
textmyself.textmyself("The message to send to my phone.)
'''

# Google: SMS Email Gateways
# SMS: Short Message Serivce
# Your option: Twilio, Free sms gateway, Python sms api, Twilio alternatives

# https://www.twilio.com/console todo left can get informations we need.
'''
from twilio.rest import Client
accountSID = 'AC58188c049628a3c82cf429a05558bd83'
authToken = "b4d4195cf24d9ab9b0a83d663ac8975a"
twilioCli = Client('accountSID, authToken)
myCellPhone = '+886921965321
myTwilioNumber = '+12166090979'
message = twilioCli.messages.create(body="今天也要好好生活喔", from_ = myTwilioNumber, to=myCellPhone)
'''

# Task Scheduler (Microsoft Windows) refernce: https://zh-tw.coderbridge.com/@JohnnyFoxChang/5ea14379cd974b78a69d41e87d10dcde
import textMyself
textMyself.textmyself("今天也請好好加油，當一個努力生活的人")
textMyself.textmyself("繼續加油吧，我很喜歡你認真的樣子")
textMyself.textmyself("再忙再累，也請不要忘記提升自己生活方面的標準")
# message.status, message.date_created, message.date_sent == None
# after received the message, message.date_sent will show None
import requests

api_address = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-AC3118BE-7C3D-481E-A522-113DA465F02F&format=JSON&locationName=%E5%98%89%E7%BE%A9%E7%B8%A3"
json_data = requests.get(api_address).json()
weather = ['0:00-6:00', '6:00-18:00', '18:00-tommorrow6:00']
for i in range(3):
    data_description = ' ' + json_data['records']['location'][0]['weatherElement'][0]['time'][i]["parameter"]["parameterName"] + '\n'#["weatherElement"]
    data_rainning = ' 降雨機率' + json_data['records']['location'][0]['weatherElement'][1]['time'][i]["parameter"]["parameterName"] + '%'  + '\n'
    data_min_temperature = '最小溫度' + json_data['records']['location'][0]['weatherElement'][2]['time'][i]["parameter"]["parameterName"] + '度c' + ' '
    data_max_temperature = '最大溫度' + json_data['records']['location'][0]['weatherElement'][4]['time'][i]["parameter"]["parameterName"] + '度c' + '\n'
    weather[i] += data_description
    weather[i] += data_rainning
    weather[i] += data_min_temperature
    weather[i] += data_max_temperature

weather_record = 'Weather Report \n'
for i in range(3):
    weather_record += weather[i]

textMyself.textmyself(weather_record)

















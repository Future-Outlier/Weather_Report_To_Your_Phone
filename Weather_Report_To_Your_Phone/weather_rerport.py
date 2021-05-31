import requests

api_address = "You have to google for the api from Central Weather Bureau"
json_data = requests.get(api_address).json()
# = json_data['records']['location'][0]['weatherElement'][0]['time'][0]["parameter"]["parameterName"]#["weatherElement"]
# for i in range(3):
#     data = json_data['records']['location'][0]['weatherElement'][0]['time'][i]["parameter"]["parameterName"]#["weatherElement"]
#     print(data)

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

weather_record = ''
for i in range(3):
    weather_record += weather[i]
print(weather_record)












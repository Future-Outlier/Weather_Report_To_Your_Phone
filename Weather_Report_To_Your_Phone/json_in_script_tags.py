import requests
import json
from bs4 import BeautifulSoup

url = "You have to google for the api from Central Weather Bureau"

r = requests.get(url)
print(r.status_code) # if 200 means ok from HTTP Response

soup = BeautifulSoup(r.content, 'html.parser')

script = soup.find_all("records")
print(script)











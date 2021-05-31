import requests
import json
from bs4 import BeautifulSoup

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-AC3118BE-7C3D-481E-A522-113DA465F02F&format=JSON&locationName=%E5%98%89%E7%BE%A9%E7%B8%A3"

r = requests.get(url)
print(r.status_code) # if 200 means ok from HTTP Response

soup = BeautifulSoup(r.content, 'html.parser')

script = soup.find_all("records")
print(script)











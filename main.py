
import requests
import json


city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=db01b69a3ee84d2880754130241701&q={city}"

r = requests.get(url)
print(r.text)
dic = json.loads(r.text)
print(dic["current"]["temp_c"])
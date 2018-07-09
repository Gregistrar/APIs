import requests
import json
import csv
import os
#import pandas as pd

api_key = "c5ecd28b1740091c1abf1b60d263efb5"

weather_url = "http://api.openweathermap.org/data/2.5/weather?q="

fileDir = os.path.dirname(os.path.realpath('__file__'))
weather_csv = "weather.csv"
file_path = os.path.join(fileDir, weather_csv)

weather_dict = {'city': [], 'temp': [], 'sky': [], 'wind': []}

with open(file_path, newline="") as csvfile:
    cities = csv.reader(csvfile, delimiter=",")
    next(cities, None)

    for row in cities:
        city = row[0]
        print("City: ", city)
        weather_dict['city'].append(city)

        call = requests.get(weather_url + city + "&appid=" + api_key + "&units=Imperial")
        call_json = call.json()

        temp = call_json['main']['temp']
        clouds = call_json['weather'][0]['description']
        wind = call_json['wind']['speed']

        print("Temp: ", temp)
        weather_dict['temp'].append(temp)
        print("Sky: ", clouds)
        weather_dict['sky'].append(clouds)
        print("Wind Speed: ", wind)
        weather_dict['wind'].append(wind)

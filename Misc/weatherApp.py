import requests
import string
from typing import Dict
import json
import pyttsx3

def text_to_speech(weather_dict,text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


city_name = input("Enter the name of the city:\n")
url = f"http://api.weatherapi.com/v1/current.json?key=168648c57a4442bb99362312251906&q={city_name}&aqi=no"

r = requests.get(url)
#print(r.text)
weather_dict = json.loads(r.text)

print(f"current temperature: {weather_dict["current"]["temp_c"]} degrees celsius")
text_to_speech(weather_dict,  f"The current temperature in {weather_dict["location"]["name"]}\
 is {weather_dict["current"]["temp_c"]} degrees celsius")

print(f"current wind speed: {weather_dict["current"]["wind_kph"]} kph")
text_to_speech(weather_dict,f"The current wind speed in {weather_dict["location"]["name"]} is\
{weather_dict["current"]["wind_kph"]} kilometers per hour")

print(f"current humidity: {weather_dict["current"]["humidity"]}")
text_to_speech(weather_dict,f"The current humidity in {weather_dict["location"]["name"]} is\
{weather_dict["current"]["humidity"]} %")
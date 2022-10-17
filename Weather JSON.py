#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""weather_forecast should return a string:
“The weather in <city> tomorow is <forecast>”
The weather_state_name key is a good description of a forecast, but how can we access it 🤔
The forecast should be for tomorrow’s date, where is that located in the response?
remember dicts built in get method to help keep your program from crashing
"""


import os; os.system("pip install requests")
import requests
response = requests.get("https://weather.lewagon.com/data/2.5/forecast?lat=51.5073219&lon=-0.1276474&units=metric").json()
# Do not modify the code above

def weather_forecast(response):
    city =  response["city"]["name"]
    forecast = response["list"]
    forecast = forecast[1]
    forecast = forecast["weather"]
    forecast = forecast[-1]
    forecast = forecast["description"]
    
    print (forecast)
    return ("The weather in " + str(city) + " tomorrow is" + forecast)


# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import datetime

print("Testing with London")
#ln = "https://www.metaweather.com/api/location/44418/"
london = {
    "city": {
        "name": "London"
    },
    "list": [
        {},
        {  "weather": [
              {
                  "id": 802,
                  "main": "Clouds",
                  "description": "scattered clouds",
              }
           ],
           "dt_txt": str(datetime.date.today() + datetime.timedelta(days=1)) + " 06:00:00"
        }
    ]
}
   
test_response = weather_forecast(london)
if "London" in test_response:
    os.system("echo '\e[32mCorrect City Name\e[0m'")
else:
    os.system("echo '\e[31mIncorrect City Name\e[0m'")
if "cloud" in test_response.lower():
    os.system("echo '\e[32mCorrect Forecast\e[0m'")
else:
    os.system("echo '\e[31mIncorrect Forecast\e[0m'")

print("Testing with San Francisco")
#sf = "https://www.metaweather.com/api/location/2487956/"
san_fran = {
    "city": {
        "name": "San Francisco"
    },
    "list": [
        {},
        {  "weather": [
              {
                  "id": 802,
                  "main": "Heavy Rain",
                  "description": "heavy rains",
              }
           ],
           "dt_txt": str(datetime.date.today() + datetime.timedelta(days=1)) + " 06:00:00"
        }
    ]
}
test_response = weather_forecast(san_fran)
if "San Francisco" in test_response:
    os.system("echo '\e[32mCorrect City Name\e[0m'")
else:
    os.system("echo '\e[31mIncorrect City Name\e[0m'")
if "rain" in test_response.lower():
    os.system("echo '\e[32mCorrect Forecast\e[0m'")
else:
    os.system("echo '\e[31mIncorrect Forecast\e[0m'")


# In[ ]:





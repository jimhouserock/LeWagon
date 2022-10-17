#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Let’s define a city_info function

city_info should take one argument, in this case our response variable
It should return a dictionary with the following keys:
‘city’ - the name of the city in response
‘lat’ - the latitude of the city in response as a float
‘lon’ - the longitude of the city in response as a float
city_info(response)
{
  'city': 'London', 
  'lat': 51.5073219,
  'lon': -0.1276474
}
"""

import os; os.system("pip install requests")
import requests
response = requests.get("https://weather.lewagon.com/geo/1.0/direct?q=london").json()
# Do not modify the code above

def city_info(response):
    city = get_value(response, "name")
    lat = get_value(response, "lat")
    lon = get_value(response, "lon")
    dict={}
    
    dict = {"city": city,"lat": lat,"lon": lon}
    return dict

def get_value(listOfDicts, key):
    for subVal in listOfDicts:
        if key in subVal:
            return subVal[key]













# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

london = requests.get("https://weather.lewagon.com/geo/1.0/direct?q=london").json()

print("Testing your function returns a dictionary")
if isinstance(city_info(london), dict):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your dictionaries keys")
if sorted(list(city_info(london).keys())) == ['city', 'lat', 'lon']:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your dictionaries values")
if city_info(london)['city'] == 'London':
    os.system("echo '\e[32mCorrect City Name\e[0m'")
else:
    os.system("echo '\e[31mIncorrect City Name\e[0m'")
if city_info(london)['lat'] == 51.5073219:
    os.system("echo '\e[32mCorrect Latitude\e[0m'")
else:
    os.system("echo '\e[31mIncorrect Latitude\e[0m'")
if city_info(london)['lon'] == -0.1276474:
    os.system("echo '\e[32mCorrect Longitude\e[0m'")
else:
    os.system("echo '\e[31mIncorrect Longitude\e[0m'")

print("Testing with a different city")
barcelona = requests.get("https://weather.lewagon.com/geo/1.0/direct?q=barcelona").json()
if city_info(barcelona)['city'] == 'Barcelona':
    os.system("echo '\e[32mCorrect City Name\e[0m'")
else:
    os.system("echo '\e[31mIncorrect City Name\e[0m'")
if city_info(barcelona)['lat'] == 41.3828939:
    os.system("echo '\e[32mCorrect Latitude\e[0m'")
else:
    os.system("echo '\e[31mIncorrect Latitude\e[0m'")
if city_info(barcelona)['lon'] == 2.1774322:
    os.system("echo '\e[32mCorrect Longitude\e[0m'")
else:
    os.system("echo '\e[31mIncorrect Longitude\e[0m'")


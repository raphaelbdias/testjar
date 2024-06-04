import requests
import geocoder
from config import openweatherapi

# Get the location information
g = geocoder.ip('142.113.124.37')
location = g.city

# Format the URL with the city name and API key
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={openweatherapi}&units=metric'

def weatherdata(url):
    res = requests.get(url)
    data = res.json()

    # Extract weather data
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    #  weather data
    data = f"""Location {location},Temperature {f"{temp}°C"},Wind {wind},Pressure {pressure}, Humidity {humidity},Description {description}."""
    return data

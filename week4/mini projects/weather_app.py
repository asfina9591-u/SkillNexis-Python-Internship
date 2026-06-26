# Weather App using OpenWeather API
import requests

API_KEY = "your_api_key_here"  # Get from openweathermap.org
city = "Udupi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error fetching weather data")

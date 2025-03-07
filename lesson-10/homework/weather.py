import requests

API_KEY = '52a2faf317dd7af5c98d22d06caa9744'
CITY = 'Tashkent'

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    
    main = data['main']
    temperature = main['temp']
    humidity = main['humidity']
    weather_description = data["weather"][0]['description']
    
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description.capitalize()}")
else:
    print(f"Failed to fetch weather data. Status code: {response.status_code}")
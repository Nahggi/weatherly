import requests
api_key = "b1a731d257200abd7d4242ab9021836a"

def get_current_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

city=""

while city!="Stop":
    city=input("Please enter city name: ")
    print(city)


    weather_data = get_current_weather(api_key, city)
    if weather_data:
        print("Weather in", city)
        print("Description:", weather_data['weather'][0]['description'])
        print("Temperature:", weather_data['main']['temp'], "°C")
        print("Humidity:", weather_data['main']['humidity'], "%")
        print("Wind Speed:", weather_data['wind']['speed'], "m/s")
    else:
        print("Failed to fetch weather data.")

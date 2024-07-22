import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def main():
    api_key = input("Enter your API key: ")
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)

    if weather_data.get('cod') != 200:
        print("Error:", weather_data.get('message'))
    else:
        print(f"Temperature in {city}: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")

if __name__ == "__main__":
    main()

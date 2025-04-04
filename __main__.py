from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        wind_speed = data['wind']['speed']

        print(f"\n--- Weather in {city.capitalize()} ---")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Weather Description: {weather_desc.capitalize()}")
    else:
        print("Error fetching weather data. Please check the city name or API key.")

def main():
    print("--- Weather Forecast Application ---")
    if not api_key:
        print("API key not found. Please set it in the .env file.")
        return

    while True:
        city = input("\nEnter the city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Exiting...")
            break
        if city:
            get_weather(city, api_key)
        else:
            print("Please enter a valid city name.")

if __name__ == "__main__":
    main()

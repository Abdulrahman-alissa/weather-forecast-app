#README.md

## weather-forecast-app

A command-line weather forecast application built with Python that fetches real-time weather data for any city using the OpenWeatherMap API.

### Features

- Get current weather details by city name
- Displays temperature, humidity, and weather description
- Handles API errors and invalid inputs gracefully
- Easily customizable and extendable for future features

#### Prerequisites

- Python 3.x
- `requests` library
- `.env` file for API key configuration

## Installation and Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Abdulrahman-alissa/weather-forecast-app.git

2. Change to the project directory:
   cd weather-forecast-app

3.Install the required Python dependencies:
pip install -r requirements.txt

4.Create a .env file in the project directory and add your OpenWeatherMap API key:
OPENWEATHER_API_KEY=your-api-key-here

5.Run the weather application:
python weather_app.py

6.Enter a city name to get the current weather details.

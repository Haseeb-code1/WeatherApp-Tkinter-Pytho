WeatherApp-Tkinter-Python

🌦️ Overview

This is a desktop weather application developed in Python using the Tkinter GUI framework. It fetches real-time weather and forecast data from the OpenWeatherMap API and displays it in an intuitive graphical interface. The app demonstrates the integration of external APIs, geolocation handling, timezone management, and object-oriented design in Python.

🔧 Features

Search for any city to get current weather data

Display temperature, humidity, wind speed, pressure, and condition

Five-day weather forecast

Automatic timezone detection based on city

Error handling for invalid input and network issues

🛠️ Technologies Used

Python 3.x

Tkinter – GUI development

OpenWeatherMap API – Weather data source

geopy – Geolocation (city to coordinates)

timezonefinder – Timezone detection

pytz – Timezone-aware datetime

requests – API requests

🚀 Getting Started

Prerequisites

Make sure you have Python 3 installed. Then install the required packages:

pip install geopy timezonefinder pytz requests

Run the App

Clone the repository and run the main script:

git clone https://github.com/Haseeb-code1/WeatherApp-Tkinter-Pytho.git
cd WeatherApp-Tkinter-Pytho
python weather_app.py

⚠️ Note: Replace weather_app.py with your actual Python script name.

🔐 API Key Setup

Replace the placeholder API key in your script with your own OpenWeatherMap API key:

self.api_key = "YOUR_API_KEY"

Sign up for a free key at: https://openweathermap.org/api

🖼️ Screenshots

![image](https://github.com/user-attachments/assets/63d32729-9c06-49eb-bd5a-37f363503d87)


🎓 Educational Value

This project helps you learn:

GUI development with Tkinter

API integration and JSON parsing

Object-Oriented Programming (OOP)

Working with external libraries in Python

Managing real-time data and handling errors

📈 Future Enhancements

Add hourly and radar forecasts

Add support for Celsius/Fahrenheit toggle

Mobile or web version using Kivy/React Native or Flask

Use charts for data visualization

🧑‍💻 Author

Haseeb Tariq – GitHub

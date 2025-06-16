from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("900x650+300+200")  # Increased height for the forecast
        self.root.resizable(False, False)
        self.api_key = "60b0f6ab7eefc9117a3c55fbee8f0ffb"  # Updated API key
        
        self.setup_ui()
    
    def setup_ui(self):
        self.search_image = PhotoImage(file="search.png")
        Label(self.root, image=self.search_image).place(x=20, y=20)

        self.textfield = Entry(self.root, justify="center", width=17, font=("popins", 25, "bold"),
                               bg="#1E1C1C", border=0, fg="white")
        self.textfield.place(x=50, y=40)
        self.textfield.focus()

        self.search_icon = PhotoImage(file="search_icon.png")
        Button(image=self.search_icon, borderwidth=0, cursor="hand2", bg="#404040",
               command=self.get_weather).place(x=400, y=34)

        self.logo_image = PhotoImage(file="logo.png")
        Label(self.root, image=self.logo_image).place(x=150, y=100)

        self.frame_image = PhotoImage(file="box.png")
        Label(self.root, image=self.frame_image).pack(padx=5, pady=5, side=BOTTOM)

        self.name_label = Label(self.root, font=("arial", 15, "bold"))
        self.name_label.place(x=30, y=100)

        self.clock = Label(self.root, font=("Helvetica", 20))
        self.clock.place(x=30, y=130)

        Label(self.root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=120, y=400)
        Label(self.root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=250, y=400)
        Label(self.root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=420, y=400)
        Label(self.root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=650, y=400)

        self.t = Label(font=("arial", 75, "bold"), fg="#ee66dd")
        self.t.place(x=400, y=150)

        self.c = Label(self.root, font=("arial", 15, "bold"))
        self.c.place(x=400, y=250)

        self.w = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
        self.w.place(x=120, y=430)

        self.h = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
        self.h.place(x=250, y=430)

        self.d = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
        self.d.place(x=420, y=430)

        self.p = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
        self.p.place(x=650, y=430)

        # Frame for 5-day forecast with rounded corners
        self.forecast_frame = Frame(self.root, bg="#1ab5ef", bd=5, relief=RAISED)
        self.forecast_frame.place(x=30, y=470, width=840, height=150)

        # Day labels for the forecast with actual dates
        self.day_labels = []
        for i in range(5):
            date_label = Label(self.forecast_frame, text="", font=("arial", 12, "bold"), bg="#1ab5ef", fg="black")
            date_label.grid(row=0, column=i, padx=10)
            self.day_labels.append(date_label)

        # Forecast labels for temperature, wind, humidity, description, and pressure
        self.forecast_labels = []
        for i in range(5):
            temp_label = Label(self.forecast_frame, text="...", font=("arial", 10), bg="#1ab5ef", fg="black")
            wind_label = Label(self.forecast_frame, text="...", font=("arial", 10), bg="#1ab5ef", fg="black")
            humidity_label = Label(self.forecast_frame, text="...", font=("arial", 10), bg="#1ab5ef", fg="black")
            desc_label = Label(self.forecast_frame, text="...", font=("arial", 10), bg="#1ab5ef", fg="black")
            pressure_label = Label(self.forecast_frame, text="...", font=("arial", 10), bg="#1ab5ef", fg="black")

            temp_label.grid(row=1, column=i, padx=5)
            wind_label.grid(row=2, column=i, padx=5)
            humidity_label.grid(row=3, column=i, padx=5)
            desc_label.grid(row=4, column=i, padx=5)
            pressure_label.grid(row=5, column=i, padx=5)

            self.forecast_labels.append((temp_label, wind_label, humidity_label, desc_label, pressure_label))

    def get_weather(self):
        city = self.textfield.get()
        geolocator = Nominatim(user_agent="my_weather_app_hori12345")

        try:
            location = geolocator.geocode(city, timeout=10)
        except Exception as e:
            messagebox.showerror("Geocoding Error", f"Error: {e}")
            return

        if not location:
            messagebox.showerror("Error", "City not found.")
            return

        try:
            tf = TimezoneFinder()
            timezone_str = tf.timezone_at(lat=location.latitude, lng=location.longitude)
            home = pytz.timezone(timezone_str)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            self.clock.config(text=current_time)
            self.name_label.config(text="Current Weather")

            # API Call for current weather
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(f"API Error {response.status_code}: {response.json().get('message')}")

            data = response.json()
            condition = data['weather'][0]['description']
            temp_celsius = round(data['main']['temp'] - 273.15, 2)
            wind = data['wind']['speed']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']

            # Display current weather information
            self.t.config(text=f"{temp_celsius}°C")
            self.c.config(text=f"{condition} | FEELS LIKE {temp_celsius}°C")
            self.w.config(text=f"{wind} m/s")
            self.h.config(text=f"{humidity}%")
            self.d.config(text=f"{condition}")
            self.p.config(text=f"{pressure} hPa")

            # Call the method to get the 5-day forecast
            self.get_forecast(city)

        except Exception as e:
            messagebox.showerror("Weather Error", f"Could not retrieve weather data.\nError: {e}")

    def get_forecast(self, city):
        try:
            # API Call for 5-day forecast
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}"
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(f"API Error {response.status_code}: {response.json().get('message')}")

            data = response.json()
            forecast_data = data['list']

            # Display the forecast for the next 5 days
            for i in range(5):
                day_data = forecast_data[i * 8]  # Get the forecast for every 24 hours
                temp_k = day_data['main']['temp']
                temp_c = round(temp_k - 273.15, 2)
                wind = day_data['wind']['speed']
                humidity = day_data['main']['humidity']
                condition = day_data['weather'][0]['description']
                pressure = day_data['main']['pressure']

                # Update the forecast labels
                self.forecast_labels[i][0].config(text=f"{temp_c}°C")  # Temperature
                self.forecast_labels[i][1].config(text=f"Wind: {wind} m/s")  # Wind
                self.forecast_labels[i][2].config(text=f"Humidity: {humidity}%")  # Humidity
                self.forecast_labels[i][3].config(text=f"Desc: {condition}")  # Description
                self.forecast_labels[i][4].config(text=f"Pressure: {pressure} hPa")  # Pressure

                # Update the date labels
                forecast_date = (datetime.now() + timedelta(days=i + 1)).strftime("%A, %B %d")
                self.day_labels[i].config(text=forecast_date)

        except Exception as e:
            messagebox.showerror("Forecast Error", f"Could not retrieve forecast data.\nError: {e}")

if __name__ == "__main__":
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()

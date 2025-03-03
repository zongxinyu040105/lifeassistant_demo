import requests
import json
import tkinter as tk
from tkinter import messagebox
def get_weather(api_key, city_code):
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city_code}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "1":
            return data["lives"][0]  
        else:
            raise Exception(f"API error: {data['info']}")
    else:
        raise Exception("Failed: {}".format(response.status_code))


def show_weather(city_code):
    api_key = "8e8bac5464e877687c853dc0cc2317cd"  
    #city_code = "370402"  
    try:
        weather_info = get_weather(api_key, city_code)
        weather_message = (
            f"Province: {weather_info['province']}\n"
            f"City: {weather_info['city']}\n"
            f"Weather: {weather_info['weather']}\n"
            f"Temperature: {weather_info['temperature']}degree\n"
            f"Humidity: {weather_info['humidity']}%"
        )
        messagebox.showinfo("Weather", weather_message)
    except Exception as e:
        messagebox.showerror("Error", str(e))

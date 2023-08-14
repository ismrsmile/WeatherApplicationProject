import requests
from tkinter import *

# API Key
api_key = "ENTER YOUR IP KEY"

def get_weather():
    city = city_name_entry.get()
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_data = data["weather"][0]
        weather_description = weather_data["description"]

        result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWeather: {weather_description}")
    else:
        result_label.config(text="City not found")


# Creation of the Window
window = Tk()
window.title("Weather Application")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# Adding Image
image_path = "weather-icon.png"
image = PhotoImage(file=image_path)
resized_image = image.subsample(2, 2)
image_label = Label(window, image=resized_image)
image_label.pack()

# Title
title_label = Label(text="Weather Application by Mr. Smile", font="Arial, 20")
title_label.pack(pady=10)

# Getting City Name from User
city_name_label = Label(text="Enter your city", font="Arial, 15")
city_name_label.pack(pady=5)

city_name_entry = Entry(width=32)
city_name_entry.pack()

# Label For Weather Results
result_label = Label(text="", font="Arial, 15", wraplength=400, justify="center")
result_label.pack(pady=10)

# Weather Button
get_weather_button = Button(text="Get Weather", font="Arial, 15", command=get_weather)
get_weather_button.pack()

window.mainloop()
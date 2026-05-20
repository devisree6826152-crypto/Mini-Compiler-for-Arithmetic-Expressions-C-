import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "d03fc4c5ff618353230b67dc5443f97b"   # ← Replace with your API key

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found!")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"].title()

        result_label.config(
            text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nDescription: {desc}"
        )

    except:
        messagebox.showerror("Error", "Failed to connect to API")


# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.config(bg="#dff6ff")

title = tk.Label(root, text="Weather Checker", font=("Arial", 18, "bold"), bg="#dff6ff")
title.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 14))
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Search Weather", font=("Arial", 12), command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#dff6ff")
result_label.pack(pady=20)

root.mainloop()

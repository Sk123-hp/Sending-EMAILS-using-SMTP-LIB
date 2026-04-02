import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = '0d85d8637ad86b655c1fb9a693b4bca7'

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Warning", "Enter city name")
        return

    # Check selected unit
    unit = unit_var.get()
    if unit == "C":
        units = "metric"
        symbol = "°C"
    else:
        units = "imperial"
        symbol = "°F"

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            result_label.config(
                text=f"City: {data['name']}\nTemp: {data['main']['temp']} {symbol}\nWeather: {data['weather'][0]['description']}"
            )
        else:
            messagebox.showerror("Error", data.get("message", "City not found"))

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("320x260")

tk.Label(root, text="Weather App", font=("Arial", 14)).pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# 🌡️ Unit selection
unit_var = tk.StringVar(value="C")

tk.Radiobutton(root, text="Celsius (°C)", variable=unit_var, value="C").pack()
tk.Radiobutton(root, text="Fahrenheit (°F)", variable=unit_var, value="F").pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
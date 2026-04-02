import requests

API_KEY = '0d85d8637ad86b655c1fb9a693b4bca7'

while True:
    city = input("\nEnter city name (or 'exit' to quit): ").strip()

    if city.lower() == 'exit':
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Details:")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
    else:
        print("❌ City not found! Try correct spelling (e.g., Islamabad)")
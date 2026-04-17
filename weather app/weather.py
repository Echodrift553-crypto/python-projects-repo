import requests

city_name = input("Enter city name: ")
api_key = ""
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"weather report for: {city_name}")
    print(f"Temperature: {temp}")
    print(f"Humidity: {humidity}")
    print(f"Description: {description}")

elif response.status_code == 404:
    print("City Not Found!")

elif response.status_code == 401:
    print("API key invalid!")

else:
    print("invalid input")
import requests

city_name = input("Enter city name: ")
# This calls your FastAPI endpoint, not the OpenWeather URL directly
response = requests.get(f"http://127.0.0.1:8000/weather/{city_name}")

print("FastAPI Response:")
print(response.json())
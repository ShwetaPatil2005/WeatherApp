"""import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("BASE_URL")

@app.get("/weather/{city}")
def get_weather(city: str):
    # Constructing the URL with the city and API key
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    return response.json()"""

import os
import requests
import mysql.connector
import json
from fastapi import FastAPI
from dotenv import load_dotenv

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins for development
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()


# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",        # Change to your MySQL username
    "password": "mysql123", # Change to your MySQL password
    "database": "A61DB"
}

@app.get("/weather/{city}")
def get_weather(city: str):
    # 1. Fetch data from OpenWeather
    params = {"q": city, "appid": os.getenv("WEATHER_API_KEY"), "units": "metric"}
    response = requests.get(os.getenv("BASE_URL"), params=params)
    data = response.json()

    if response.status_code == 200:
        # 2. Save to MySQL
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            query = """
                INSERT INTO weather_logs (city_name, temperature, humidity, description, json_data)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                data['name'], 
                data['main']['temp'], 
                data['main']['humidity'], 
                data['weather'][0]['description'],
                json.dumps(data) # Saving the full raw JSON
            )
            
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            print("Data saved to MySQL successfully!")
        except Exception as e:
            print(f"Database Error: {e}")

    return data

@app.get("/weather/coords/")
def get_weather_by_coords(lat: float, lon: float):
    # Use lat/lon instead of q in params
    params = {
        "lat": lat, 
        "lon": lon, 
        "appid": os.getenv("WEATHER_API_KEY"), 
        "units": "metric"
    }
    response = requests.get(os.getenv("BASE_URL"), params=params)
    data = response.json()

    if response.status_code == 200:
        # Reusing your MySQL logic from earlier
         # 2. Save to MySQL
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            query = """
                INSERT INTO weather_logs (city_name, temperature, humidity, description, json_data)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                data['name'], 
                data['main']['temp'], 
                data['main']['humidity'], 
                data['weather'][0]['description'],
                json.dumps(data) # Saving the full raw JSON
            )
            
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            print("Data saved to MySQL successfully!")
        except Exception as e:
            print(f"Database Error: {e}")
        
    return data
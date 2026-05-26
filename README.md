# 🌦 Weather API Application using FastAPI, Docker & Jenkins

## 📌 Project Overview
This project is a Weather Data Fetching Application developed using FastAPI.  
It fetches real-time weather information from the OpenWeather API and stores weather logs into a MySQL database.

The project also demonstrates:
- REST API development
- Docker containerization
- Jenkins CI/CD integration
- Swagger UI testing
- GitHub version control

---

## 🚀 Technologies Used

- FastAPI
- Python
- Docker
- Jenkins
- MySQL
- OpenWeather API
- Swagger UI
- GitHub

---

## 📂 Project Structure

```bash
WeatherAPI/
│
├── main.py
├── requirement.txt
├── Dockerfile
├── .env
├── .gitignore
├── README.md
├── client.py
└── index.html
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv virtualenv
```

### 2️⃣ Activate Virtual Environment

```bash
virtualenv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirement.txt
```

---

## ▶️ Run FastAPI Application

```bash
uvicorn main:app --reload
```

---

## 🌐 Swagger UI

Open browser:

```bash
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Commands

### Build Docker Image

```bash
docker build -t weather-api-app .
```

### Run Docker Container

```bash
docker run -p 8000:8000 weather-api-app
```

---

## 🔧 Jenkins Integration

### Jenkins Build Command

```bash
D:
cd D:\WebDevelopment\Experiment9.1\WeatherAPI

docker build -t weather-api-app .

docker run -p 8000:8000 weather-api-app
```

---

## 📡 API Endpoints

### Get Weather by City

```bash
GET /weather/{city}
```

Example:

```bash
http://127.0.0.1:8000/weather/Pune
```

---

### Get Weather by Coordinates

```bash
GET /weather/coords/?lat=18.5204&lon=73.8567
```

---

## 📊 Features

- Real-time weather fetching
- Weather data logging
- Coordinate-based weather search
- Interactive Swagger UI
- Dockerized deployment
- Jenkins automation
- REST API integration

---

## 👩‍💻 Developed By

Shweta Pradeep Patil

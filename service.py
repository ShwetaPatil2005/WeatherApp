import bentoml
import numpy as np
from sklearn.linear_model import LinearRegression

# Load model
model = bentoml.sklearn.load_model("weather_prediction_model:latest")

# Create BentoML service
@bentoml.service
class WeatherPredictionService:

    @bentoml.api
    def predict(self, humidity: float) -> dict:

        data = np.array([[humidity]])

        prediction = model.predict(data)

        return {
            "predicted_temperature": float(prediction[0])
        }
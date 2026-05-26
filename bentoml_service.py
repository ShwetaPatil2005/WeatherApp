import bentoml
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample training data
data = {
    "humidity": [30, 40, 50, 60, 70, 80, 90],
    "temperature": [35, 33, 30, 28, 25, 22, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["humidity"]]
y = df["temperature"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model in BentoML
bentoml.sklearn.save_model("weather_prediction_model", model)

print("Model saved successfully in BentoML!")
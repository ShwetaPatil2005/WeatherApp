import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

# Sample weather dataset
data = {
    "humidity": [30, 40, 50, 60, 70, 80, 90],
    "temperature": [35, 33, 30, 28, 25, 22, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Labels
X = df[["humidity"]]
y = df["temperature"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Start MLFlow experiment
mlflow.set_experiment("Weather Temperature Prediction")

with mlflow.start_run():

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prediction
    predictions = model.predict(X_test)

    # Calculate error
    mse = mean_squared_error(y_test, predictions)

    # Log parameters
    mlflow.log_param("model_type", "LinearRegression")

    # Log metric
    mlflow.log_metric("mse", mse)

    # Log model
    mlflow.sklearn.log_model(model, "weather_model")

    print("Model trained successfully!")
    print("MSE:", mse)
import argparse
import joblib
import numpy as np
import os

# Argument parser
parser = argparse.ArgumentParser(description="Predict ice cream sales based on temperature")
parser.add_argument("--temperature", type=float, required=True, help="Temperature in Celsius")
args = parser.parse_args()

# Load model
model_path = os.path.join("outputs", "model.joblib")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

model = joblib.load(model_path)

# Predict
temperature_input = np.array([[args.temperature]])
prediction = model.predict(temperature_input)

# Output result
print(f"🌡️ Temperature: {args.temperature}°C")
print(f"🍦 Predicted ice cream sales: {prediction[0]:.2f} units")

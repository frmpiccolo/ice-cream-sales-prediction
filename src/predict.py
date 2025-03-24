import argparse
import joblib
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--temperature", type=float, required=True)
args = parser.parse_args()

model = joblib.load("outputs/model.joblib")
prediction = model.predict(np.array([[args.temperature]]))
print(f"Predicted ice cream sales: {prediction[0]:.2f}")

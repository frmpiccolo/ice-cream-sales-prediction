import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
import joblib

data = pd.read_csv("data/ice_cream_sales.csv")
X = data[["temperature"]]
y = data["sales"]

model = LinearRegression()
model.fit(X, y)

mlflow.sklearn.log_model(model, "ice_cream_model")
joblib.dump(model, "outputs/model.joblib")
print("Model trained and saved.")

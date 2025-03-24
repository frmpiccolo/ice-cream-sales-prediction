import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
import joblib

# Try to detect Azure ML context
try:
    from azureml.core import Run, Workspace, Dataset
    run = Run.get_context()
    if hasattr(run, 'experiment'):
        ws = run.experiment.workspace
        running_in_azure = True
    else:
        raise Exception("Offline run")
except:
    run = None
    ws = None
    running_in_azure = False

print("🔍 Running in Azure ML Studio:" if running_in_azure else "💻 Running locally")

# Load dataset accordingly
if running_in_azure and ws:
    dataset = Dataset.get_by_name(ws, name='ice_cream_sales')
    data = dataset.to_pandas_dataframe()
else:
    data = pd.read_csv("data/ice_cream_sales.csv")

# Prepare data
X = data[["temperature"]]
y = data["sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Log model if MLflow is active
mlflow.sklearn.log_model(model, "ice_cream_model")

# Save model
os.makedirs("outputs", exist_ok=True)
joblib.dump(model, "outputs/model.joblib")

print("✅ Model trained and saved.")

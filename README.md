# Ice Cream Sales Forecasting with Azure ML and MLflow 🍦📊

Forecast daily ice cream sales based on temperature using a machine learning regression model. The project uses Azure Machine Learning and MLflow for experiment tracking and model deployment.

---

## 🔍 Project Overview

This project simulates a real-world scenario where an ice cream shop owner uses machine learning to optimize production based on temperature. By predicting daily sales, the owner can reduce waste and maximize profit.

---

## 🎯 Objectives

- ✅ Train a regression model using historical temperature and sales data
- ✅ Log the model using MLflow
- ✅ Deploy the model to Azure for real-time predictions
- ✅ Structure the project using best practices (pipelines, reproducibility)

---

## 🗂️ Project Structure

```
ice-cream-sales-prediction/
├── data/
│   └── ice_cream_sales.csv          # Example dataset
├── src/
│   ├── train.py                     # Script to train the model and log with MLflow
│   └── predict.py                   # Script to run predictions
├── inputs/
│   └── example_sentences.txt        # As per the project challenge
├── notebooks/
│   └── exploratory_analysis.ipynb   # Optional: EDA in notebook format
├── azure/
│   └── aml_config.json              # Azure ML workspace config
├── README.md                        # Complete documentation
└── requirements.txt                 # Python dependencies
```

---

## 🧪 Example Dataset

Located in `data/ice_cream_sales.csv`, this dataset contains historical temperature and corresponding daily sales.

---

## ⚙️ Setup Instructions

### 1. Prerequisites

- Python 3.8+
- An [Azure subscription](https://portal.azure.com/)
- VS Code with Azure ML and Python extensions
- Git

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ice-cream-sales-prediction.git
cd ice-cream-sales-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Azure ML Workspace

1. Create a new Azure ML Workspace in the Azure Portal
2. Download your `config.json` file and save it to `azure/aml_config.json`

### 5. Connect and Submit Experiments

Use `train.py` to train and log the model:

```bash
python src/train.py
```

This script:
- Trains a regression model
- Logs parameters, metrics, and model artifacts in MLflow
- Saves the model to the `outputs/` folder

### 6. Deploy the Model to Azure

(Optional) Register and deploy the model using Azure ML SDK or portal:
- Register the model
- Create an inference configuration
- Deploy to a container instance or AKS

### 7. Run Predictions

Use the `predict.py` script with a temperature value:

```bash
python src/predict.py --temperature 32
```

---

## 📝 Example Inputs

The `inputs/example_sentences.txt` file contains example use cases, questions, and insights gained during model exploration.

---

## 📊 Insights and Learnings

- There is a strong linear correlation between temperature and sales
- Simple regression models like `LinearRegression` can perform well in small datasets
- Azure ML and MLflow streamline training, logging, and deployment

---

## 📸 Screenshots

(Add screenshots here showing: model training output, MLflow logs, prediction results)

---

## ⚠️ Disclaimer on Azure Costs

> **Important**: This project uses Azure Machine Learning, which may incur costs depending on your resource usage. Always monitor your resource consumption in the Azure portal and stop compute instances when not in use.

Free-tier resources are available but limited. Use [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to estimate potential costs.

---

## 🚀 Future Enhancements

- Add forecast using weather API
- Use time-series forecasting models
- Create a dashboard for sales visualization

---

## 📬 Contact

Created by [Fermin Piccolo](https://www.linkedin.com/in/ferminpiccolo)

# Diabetes Regression

## About This Project

This project uses the `Diabetes_Dataset.csv` file to predict diabetes progression or related health score using patient clinical features.

## Files Included

- `Diabetes_Dataset.csv` — dataset with diabetes-related clinical variables
- `Diabetes_regression.ipynb` — notebook with data preparation and regression modeling
- `README.md` — this file

## Dataset Notes

- The dataset contains clinical measurements such as age, BMI, blood pressure, and other medical variables.
- The goal is to predict a continuous outcome related to diabetes progression.

## How to Run

1. Open `Diabetes_regression.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab.
2. Confirm that `Diabetes_Dataset.csv` is in the same folder.
3. Execute all notebook cells in order.

## Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## What this Notebook Covers

- Loading and inspecting medical data
- Visualizing feature distributions
- Training a linear regression model
- Evaluating predictions using MAE, MSE, RMSE, and R²
- Discussing model accuracy and improvement ideas

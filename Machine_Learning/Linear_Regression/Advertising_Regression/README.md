# Advertising Regression

## About This Project

This project uses the `Advertising.csv` dataset to predict product sales from advertising budgets spent on TV, radio, and newspaper media.

## Files Included

- `Advertising.csv` — dataset with advertising budget and sales values
- `advertising_regression.ipynb` — notebook with data analysis, model training, and evaluation
- `README.md` — this file

## Dataset Notes

- The dataset includes the following columns:
  - `TV`
  - `Radio`
  - `Newspaper`
  - `Sales`
- The target variable is `Sales`, which measures product sales in thousands of units.

## How to Run

1. Open `advertising_regression.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab.
2. Make sure `Advertising.csv` is saved in the same folder.
3. Run the notebook cells sequentially.

## Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## What this Notebook Covers

- Data loading and exploration
- Visual analysis of advertising channels
- Correlation analysis
- Linear regression modeling
- Model evaluation with RMSE, MAE, and R²
- Interpretation of coefficients

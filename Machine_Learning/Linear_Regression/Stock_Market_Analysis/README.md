# Stock Market Closing Price Prediction — Linear Regression

## Project Overview

This project applies Machine Learning (Linear Regression) to predict stock closing prices using historical market data. The dataset covers 5 major companies from 2019 to 2024, containing 7,825 trading day records with financial indicators like opening price, high, low, volume, and adjusted close.

## Dataset Information

- **Source:** Simulated historical stock market data
- **Samples:** 7,825 records
- **Companies:** AAPL, GOOGL, MSFT, AMZN, TSLA
- **Date Range:** January 2019 – December 2024
- **Target Variable:** Close (Closing Price)
- **Missing Values:** None
- **Data Type:** Numerical

### Column Descriptions

| Column | Description |
|--------|-------------|
| Date | Trading date (YYYY-MM-DD) |
| Company | Stock ticker symbol |
| Open | Opening price of the day ($) |
| High | Highest price during the day ($) |
| Low | Lowest price during the day ($) |
| Close | Closing price of the day (Target) ($) |
| Volume | Number of shares traded |
| Adj_Close | Adjusted closing price ($) |

### Engineered Features (Created in Notebook)

| Feature | Formula | Description |
|---------|---------|-------------|
| Price_Range | High - Low | Daily price spread |
| Price_Change | Close - Open | Daily price movement |
| Avg_Price | (High + Low) / 2 | Average of high and low |
| Company_Encoded | LabelEncoder | Numeric company identifier |

## Project Structure

```
├── Stock_Market_Dataset.csv                  # Dataset (7,825 rows, 8 columns)
├── Stock_Market_ML_Linear_Regression.ipynb   # Jupyter Notebook with full analysis
└── README.md                                 # Project documentation
```

## Notebook Sections

1. **Import Libraries** — NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
2. **Load Dataset** — Read CSV into DataFrame
3. **Basic Info & Statistics** — Info, describe, null check, duplicates, records per company
4. **Exploratory Data Analysis** — Distribution plots, price trends, volume boxplot, correlation heatmap, scatter plots, average close bar chart, daily range boxplot
5. **Feature Engineering** — Price_Range, Price_Change, Avg_Price, Company encoding
6. **Data Preprocessing** — StandardScaler + 80/20 train-test split
7. **Model Training** — Linear Regression with coefficient analysis and visualization
8. **Predictions** — Actual vs Predicted comparison table
9. **Model Evaluation** — MAE, MSE, RMSE, R² with overfitting check
10. **Result Visualizations** — Scatter plot, residual plot, residual distribution, line overlay, error metrics bar chart
11. **Per-Company Performance** — R² and MAE breakdown for each company
12. **Summary** — Key findings and conclusions

## How to Run

### Option 1: Google Colab
1. Upload both `Stock_Market_Dataset.csv` and `Stock_Market_ML_Linear_Regression.ipynb` to Colab
2. Make sure the CSV is in the same directory or update the path
3. Run all cells

### Option 2: Local Jupyter
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
jupyter notebook Stock_Market_ML_Linear_Regression.ipynb
```

## Requirements

- Python 3.8+
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Key Findings

- **Open, High, Low** and **Adj_Close** are the strongest predictors of closing price
- **Volume** has a relatively weak correlation with closing price
- Linear Regression achieves very high R² due to the strong linear relationship between OHLC price features
- Residuals follow a normal distribution, confirming the model assumptions are valid
- Model performance is consistent across all five companies

## Model Used

| Model | Type | Task |
|-------|------|------|
| Linear Regression | Supervised ML | Regression |

## Evaluation Metrics

| Metric | Description |
|--------|-------------|
| MAE | Mean Absolute Error — average absolute difference between actual and predicted |
| MSE | Mean Squared Error — average squared difference, penalizes large errors |
| RMSE | Root Mean Squared Error — square root of MSE, same unit as target |
| R² | Coefficient of Determination — proportion of variance explained by the model |

## Companies in Dataset

| Ticker | Company |
|--------|---------|
| AAPL | Apple Inc. |
| GOOGL | Alphabet Inc. |
| MSFT | Microsoft Corporation |
| AMZN | Amazon.com Inc. |
| TSLA | Tesla Inc. |

## Author

**Tabasum Amin**

## License

This project and dataset are created for educational and research purposes.

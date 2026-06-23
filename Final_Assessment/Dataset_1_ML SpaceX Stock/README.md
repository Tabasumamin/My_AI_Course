# SpaceX Stock Price ML Project

## Project Overview

This project is based on SpaceX stock price data. In this notebook, I explored the stock dataset and used machine learning models to practice prediction and classification tasks.

The main goal was to understand the data, create useful features, train different models, compare their results, and save the final models.

## Dataset

The dataset used in this project is:

```text
data/raw/spacex.csv
```

The dataset contains stock data at 30-minute intervals. It includes columns such as datetime, open price, high price, low price, close price, and volume.

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle

## Project Steps

1. Loaded the SpaceX stock dataset.
2. Converted the datetime column into proper date-time format.
3. Checked basic statistics and missing values.
4. Created visualizations for close price, volume, price range, and correlations.
5. Added new features such as price range, price change, direction, rolling close value, and hour.
6. Trained regression models to predict close price.
7. Trained classification models to predict price direction.
8. Used KMeans clustering to group similar stock records.
9. Compared ensemble learning models.
10. Saved the trained models.

## Models Used

### Regression

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Classification

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Clustering

- KMeans Clustering

### Ensemble Learning

- Random Forest
- Gradient Boosting
- AdaBoost
- Bagging

## Saved Models

The trained models are saved inside the `models` folder:

```text
models/model_regressor.pkl
models/model_classifier.pkl
models/model_ensemble.pkl
```

## How to Run

Open `Dataset_1_ML_SpaceX_Stock.ipynb` and run all cells from top to bottom. Make sure `spacex.csv` is available inside the `data/raw` folder.

## Important Note

This project is for learning and practice. Stock data can change quickly, so the results should not be used as financial advice.

## Conclusion

In this project, I learned how to analyze stock data, create new features, train machine learning models, compare model results, and save models for later use.

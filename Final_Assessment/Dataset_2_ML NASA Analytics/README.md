# NASA Analytics 2010-2024 ML Project

## Project Overview

This project is based on NASA analytics data from 2010 to 2024. In this notebook, I explored the dataset and used machine learning models to understand yearly NASA activity and budget patterns.

The main goal was to practice data loading, EDA, feature engineering, regression, classification, clustering, ensemble learning, and saving trained models.

## Dataset

The dataset used in this project is:

```text
data/raw/Nasa_Analytics_2010_2024.csv
```

The dataset contains 15 records, one for each year from 2010 to 2024. It includes columns such as year, launches, successful launches, failed launches, budget funding, employees, rockets, and success rate.

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle

## Project Steps

1. Loaded the NASA analytics dataset.
2. Checked descriptive statistics and missing values.
3. Created visualizations for launches, budget, employees, rockets, and correlations.
4. Added new features such as budget per launch, employee per rocket, launch growth, and high activity label.
5. Trained regression models to predict NASA budget funding.
6. Trained classification models to predict high or low activity years.
7. Used KMeans clustering to group similar years.
8. Compared ensemble learning models.
9. Saved the best trained models using pickle.

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
models/nasa_regressor.pkl
models/nasa_classifier.pkl
models/nasa_ensemble.pkl
```

## How to Run

Open `Dataset _2 _ML_NASA_Analytics.ipynb` and run all cells from top to bottom. Make sure the CSV file is available inside the `data/raw` folder before running the notebook.

## Important Note

The dataset is small, so model performance can change easily depending on the train-test split. The main purpose of this project is to understand and practice the machine learning workflow.

## Conclusion

In this project, I learned how to clean and explore data, create useful features, train different machine learning models, compare results, perform clustering, and save final models.

# Dataset 1: Predict Students' Dropout and Academic Success

## About This Dataset

Higher education student data compiled from multiple institutional databases. Each record represents one student and includes enrollment details, demographic background, socio-economic factors, and academic performance across two semesters.

## Task

Three-class classification — predict whether a student will Drop Out, stay Enrolled, or Graduate.

## Dataset Details

| Property | Value |
|---|---|
| Instances | 4,424 |
| Features | 36 |
| Target Classes | 3 (Dropout, Enrolled, Graduate) |
| Data Format | Tabular (CSV) |
| Class Balance | Imbalanced |

## Files Included

| File | Description |
|---|---|
| students_dropout.csv | Full dataset with 36 features and target column |
| Students_Dropout_Classification.ipynb | Complete ML pipeline notebook |
| README.md | This file |

## Feature Groups

- Academic Path: application mode, course, previous qualifications, admission grade
- Demographics: age, gender, nationality, marital status
- Socio-Economic: parental education, occupation, scholarship, debtor status
- Semester Performance: enrolled units, approved units, grades (1st and 2nd semester)
- Macroeconomic: unemployment rate, inflation rate, GDP

## How to Run

1. Place the CSV file in the same directory as the notebook
2. Open the notebook in Jupyter or Google Colab
3. Run cells sequentially from top to bottom
4. Install imbalanced-learn if you want to run the SMOTE section: pip install imbalanced-learn

## Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- imbalanced-learn (optional, for SMOTE)

## What the Notebook Covers

- Exploratory Data Analysis with visualizations
- Class imbalance analysis and handling (class weights, SMOTE)
- Feature importance and selection
- Baseline model (Logistic Regression)
- Model comparison (Random Forest, Gradient Boosting, SVM)
- Stratified cross-validation
- Confusion matrix analysis

## Key Learning Outcomes

- Handling class imbalance in multiclass problems
- Choosing the right evaluation metric (Macro F1 over accuracy)
- Feature selection on wide tabular datasets
- Comparing multiple classifiers with proper validation

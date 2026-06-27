# Dataset 3: Multivariate Gait Data Classification

## About This Dataset

Biomechanical gait data from 10 healthy subjects walking under three conditions — unbraced (normal), knee braced, and ankle braced. Bilateral joint angle measurements (ankle, knee, hip) are recorded across consecutive gait cycles.

## Task

Sequence classification — predict the walking condition (Unbraced, Knee Braced, Ankle Braced) from joint angle patterns. Also supports regression and clustering experiments.

## Dataset Details

| Property | Value |
|---|---|
| Instances | 181,800 |
| Features | 7 (time-series channels) |
| Target Classes | 3 (Unbraced, Knee Braced, Ankle Braced) |
| Data Format | Sequential, Multivariate Time-Series (CSV) |
| Subjects | 10 |
| Gait Cycles | 10 per condition per subject |

## Files Included

| File | Description |
|---|---|
| gait_data.csv | Full time-series dataset with all joint angles |
| Gait_Data_Classification.ipynb | Complete ML pipeline notebook |
| README.md | This file |

## Features

- Subject_ID: Subject identifier (1-10)
- Condition: Walking condition (target variable)
- Gait_Cycle: Cycle number (1-10)
- Time_Percent: Position within the gait cycle (0-100%)
- Ankle_Left: Left ankle joint angle (degrees)
- Ankle_Right: Right ankle joint angle (degrees)
- Knee_Left: Left knee joint angle (degrees)
- Knee_Right: Right knee joint angle (degrees)
- Hip_Left: Left hip joint angle (degrees)
- Hip_Right: Right hip joint angle (degrees)

## How to Run

1. Place the CSV file in the same directory as the notebook
2. Open the notebook in Jupyter or Google Colab
3. Run cells sequentially from top to bottom
4. The notebook uses standard libraries — no special installs needed

## Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## What the Notebook Covers

- Gait cycle visualization across conditions and subjects
- Statistical feature extraction per gait cycle (mean, std, min, max, range, skew, kurtosis)
- Multiple classifiers (Random Forest, SVM, Gradient Boosting, KNN)
- Feature importance analysis for joint angle features
- Leave-one-subject-out cross-validation for generalization testing
- Standard CV vs LOSO CV comparison
- Confusion matrix analysis

## Key Learning Outcomes

- Converting multivariate time-series into tabular features for classification
- Understanding feature engineering on sequential biomechanical data
- The critical difference between standard CV and leave-one-subject-out CV
- Why subject generalization matters in biomedical ML applications
- Identifying which joints and statistical measures drive classification

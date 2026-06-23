# SpaceX Missions Analysis

## Project Overview

This project is based on SpaceX mission data. In this notebook, I explored the dataset and trained RNN, LSTM, and GRU models to practice working with sequence data.

## Dataset

The dataset file is:

```text
data/raw/database.csv
```

The dataset has 41 records and includes mission details like flight number, launch date, launch site, vehicle type, payload details, customer information, mission outcome, and landing outcome.

## Libraries Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras

## Work Done

1. Loaded and checked the SpaceX dataset.
2. Viewed basic statistics and missing values.
3. Created graphs for mission outcome and other columns.
4. Prepared the data for model training.
5. Trained RNN, LSTM, and GRU models.
6. Compared the models using MAE and R2 score.
7. Saved the trained models.

## Saved Models

```text
rnn_spacex.h5
lstm_spacex.h5
gru_spacex.h5
```

## How to Run

Open `Dataset_3_DL_SpaceX_Missions.ipynb` and run all cells from top to bottom. Make sure `database.csv` is available inside the `data/raw` folder.

## Conclusion

In this project, I learned how to clean and prepare mission data, create simple visualizations, train sequence models, and compare their results.

# NASA Analytics 2010-2024

## Project Overview

This project is based on NASA analytics data from 2010 to 2024. In this notebook, I analyzed yearly NASA data and used deep learning models to predict budget funding values.

## Dataset

The dataset used in this project is:

```text
data/raw/Nasa_Analytics_2010_2024.csv
```

The dataset has 15 records, one for each year from 2010 to 2024. It includes columns like year, launches, successful launches, failed launches, budget funding, employees, rockets, and success rate.

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras

## Project Steps

1. Loaded and checked the NASA dataset.
2. Performed basic EDA using graphs and a correlation heatmap.
3. Scaled the selected features using `MinMaxScaler`.
4. Created time series sequences using previous years of data.
5. Trained RNN, LSTM, and GRU models.
6. Compared the models using MAE and model score.
7. Saved the trained models.

## Models Used

In this project, I used three deep learning models:

- Simple RNN
- LSTM
- GRU

After training, the saved model files are:

```text
rnn_nasa.h5
lstm_nasa.h5
gru_nasa.h5
```

## How to Run

Open `Dataset_4_DL_NASA Analytics.ipynb` and run all cells from top to bottom. Make sure the CSV file is available inside the `data/raw` folder before running the notebook.

## Important Note

The dataset is small, so the model performance may not be very strong. The main purpose of this project is to understand the deep learning workflow for time series type data.

## Conclusion

In this project, I learned how to prepare data, create sequences, train RNN-based models, compare results, and save trained models.

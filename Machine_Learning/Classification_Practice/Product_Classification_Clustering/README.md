# Dataset 2: Product Classification and Clustering

## About This Dataset

Product offer data collected from PriceRunner, a product comparison platform. Contains product listings across 10 categories from 306 different merchants, with textual descriptions and metadata.

## Task

Multi-class text classification — assign each product offer to the correct category based on title and description. Also supports clustering and entity matching experiments.

## Dataset Details

| Property | Value |
|---|---|
| Instances | 35,311 |
| Features | 7 |
| Target Classes | 10 categories |
| Data Format | Tabular + Text (CSV) |
| Merchants | 306 |

## Files Included

| File | Description |
|---|---|
| product_classification.csv | Full dataset with product text and categories |
| Product_Classification.ipynb | Complete ML pipeline notebook |
| README.md | This file |

## Categories

Electronics, Clothing, Home and Garden, Sports, Books, Toys, Automotive, Health and Beauty, Food and Grocery, Office Supplies

## Features

- Product_ID: Unique identifier for each product offer
- Product_Title: Short text title of the product
- Category: Target label (10 classes)
- Merchant: Merchant name
- Price: Product price
- Brand: Brand name
- Description: Longer text description

## How to Run

1. Place the CSV file in the same directory as the notebook
2. Open the notebook in Jupyter or Google Colab
3. Run cells sequentially from top to bottom
4. All required libraries are standard scikit-learn — no special installs needed

## Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## What the Notebook Covers

- Text preprocessing and cleaning
- TF-IDF feature extraction with n-grams
- Top terms analysis per category
- Classification models (Naive Bayes, Linear SVM, Logistic Regression)
- K-Means clustering with ARI and NMI evaluation
- PCA visualization of category clusters
- Stratified cross-validation comparison

## Key Learning Outcomes

- Building classification models on short text data
- TF-IDF vectorization with tuned parameters
- Comparing text classifiers (NB vs SVM vs LR)
- Evaluating unsupervised clustering against known labels
- Understanding how text feature quality impacts classification performance

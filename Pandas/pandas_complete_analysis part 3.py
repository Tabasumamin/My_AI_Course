# ============================================
# Pandas Assignment - Real Estate Dataset
# ============================================

# 1. Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Loading Dataset
df = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv')

# 3. Basic Exploration
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nFirst 5 rows:")
print(df.head())

# 4. Dataset Info
print("\nDataset Info:")
df.info()

# 5. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 6. Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 7. Data Cleaning
df.dropna(inplace=True)
print("\nAfter cleaning shape:", df.shape)

# 8. NumPy Operations
print("\nNumPy Operations:")
print("Mean Sale Amount:", np.mean(df['Sale Amount']))
print("Max Sale Amount:", np.max(df['Sale Amount']))
print("Min Sale Amount:", np.min(df['Sale Amount']))
print("Std Sale Amount:", np.std(df['Sale Amount']))

# 9. Pandas Operations
print("\nValue Counts - Property Type:")
print(df['Property Type'].value_counts())

print("\nValue Counts - Town:")
print(df['Town'].value_counts().head(10))

# 10. Groupby Operation
print("\nAverage Sale Amount by Property Type:")
print(df.groupby('Property Type')['Sale Amount'].mean())

# 11. Visualization 1 - Property Type Count
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Property Type')
plt.title('Count by Property Type')
plt.xticks(rotati)
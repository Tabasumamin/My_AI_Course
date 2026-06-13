# ============================================
# Seaborn Complete Analysis
# RealEstate USA Dataset
# ============================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Loading Dataset
df = pd.read_csv(r'C:\Users\Adnan Computer\Documents\GitHub\My_AI_Course\RealEstate-USA.csv')
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nFirst 5 rows:")
print(df.head())

# 2. Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Data Cleaning
df.dropna(inplace=True)
print("\nAfter cleaning shape:", df.shape)

# 4. Basic Plot - Count by State
plt.figure(figsize=(12,5))
sns.countplot(data=df, y='state', 
              order=df['state'].value_counts().index[:15])
plt.title('Top 15 States by Property Count')
plt.show()

# 5. Distribution Plot - Price
plt.figure(figsize=(10,5))
sns.histplot(data=df, x='price', bins=50)
plt.title('Property Price Distribution')
plt.xlabel('Price')
plt.show()

# 6. Categorical Plot - Property Type
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='propertyType',
              order=df['propertyType'].value_counts().index)
plt.title('Count by Property Type')
plt.xticks(rotation=45)
plt.show()

# 7. Relationship Plot - Price vs Beds
plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='beds',)
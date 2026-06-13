# ============================================
# Seaborn Complete Analysis
# FastFood Restaurants Dataset
# ============================================

# 1. Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Loading Dataset
df = pd.read_csv('FastFoodRestaurants.csv')
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nFirst 5 rows:")
print(df.head())

# 3. Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Basic Plot - Count of Restaurants by Province
plt.figure(figsize=(12,5))
sns.countplot(data=df, x='province')
plt.title('Restaurant Count by Province')
plt.xticks(rotation=45)
plt.show()

# 5. Categorical Plot - Restaurant by Category
plt.figure(figsize=(12,5))
sns.countplot(data=df, x='categories')
plt.title('Restaurant Count by Category')
plt.xticks(rotation=90)
plt.show()

# 6. Distribution Plot
plt.figure(figsize=(10,5))
sns.histplot(data=df, x='postalCode', bins=50)
plt.title('Postal Code Distribution')
plt.show()

# 7. Relationship Plot
plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='longitude', y='latitude', 
                hue='province')
plt.title('Restaurant Locations')
plt.show()

# 8. Heatmap - Correlation
plt.figure(figsize=(8,6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 9. Box Plot
plt.figure(figsize=(12,5))
sns.boxplot(data=df, x='province', y='postalCode')
plt.title('Postal Code by Province')
plt.xticks(rotation=45)
plt.show()

# 10. Value Counts
print("\nTop 10 Cities:")
print(df['city'].value_counts().head(10))

print("\nTop Categories:")
print(df['categories'].value_counts().head(10))
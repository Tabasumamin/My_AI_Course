# ============================================
# Seaborn Complete Analysis
# Startup Growth Investment Dataset
# ============================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Loading Dataset
df = pd.read_csv(r'C:\Users\Adnan Computer\Documents\GitHub\My_AI_Course\startup_growth_investment_data.csv')
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

# 4. Basic Plot - Count by Industry
plt.figure(figsize=(12,5))
sns.countplot(data=df, x='Industry',
              order=df['Industry'].value_counts().index)
plt.title('Startup Count by Industry')
plt.xticks(rotation=45)
plt.show()

# 5. Distribution Plot - Investment Amount
plt.figure(figsize=(10,5))
sns.histplot(data=df, x='Investment_Amount_USD', bins=50)
plt.title('Investment Amount Distribution')
plt.xlabel('Investment Amount (USD)')
plt.show()

# 6. Categorical Plot - Funding Stage
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Funding_Stage',
              order=df['Funding_Stage'].value_counts().index)
plt.title('Count by Funding Stage')
plt.xticks(rotation=45)
plt.show()

# 7. Relationship Plot - Investment vs Revenue
plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='Investment_Amount_USD',
                y='Revenue_USD', hue='Industry')
plt.title('Investment vs Revenue')
plt.show()

# 8. Box Plot - Investment by Industry
plt.figure(figsize=(12,5))
sns.boxplot(data=df, x='Industry',
            y='Investment_Amount_USD')
plt.title('Investment Amount by Industry')
plt.xticks(rotation=45)
plt.show()

# 9. Heatmap - Correlation
plt.figure(figsize=(8,6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True,
            fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 10. Bar Plot - Average Investment by Industry
plt.figure(figsize=(12,5))
df.groupby('Industry')['Investment_Amount_USD'].mean(
    ).sort_values(ascending=False).plot(kind='bar')
plt.title('Average Investment by Industry')
plt.xlabel('Industry')
plt.ylabel('Average Investment (USD)')
plt.xticks(rotation=45)
plt.show()

# 11. Value Counts
print("\nTop Industries:")
print(df['Industry'].value_counts())
print("\nFunding Stages:")
print(df['Funding_Stage'].value_counts())
print("\nAverage Investment by Industry:")
print(df.groupby('Industry')[
    'Investment_Amount_USD'].mean())
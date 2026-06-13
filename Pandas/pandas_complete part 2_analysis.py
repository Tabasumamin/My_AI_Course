# ============================================
# NumPy & Pandas Assignment - Startup Dataset
# ============================================

# 1. Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Loading Dataset
df = pd.read_csv('startup_growth_investment_data.csv')

# 3. Basic Exploration
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nFirst 5 rows:")
df.head()

# 4. Dataset Info
df.info()

# 5. Statistical Summary
df.describe()

# 6. Missing Values
print("\nMissing Values:")
df.isnull().sum()

# 7. Data Cleaning
df.dropna(inplace=True)
print("\nAfter cleaning shape:", df.shape)

# 8. NumPy Operations
print("\nNumPy Operations:")
print("Mean Investment:", np.mean(df['Investment_Amount_USD']))
print("Max Investment:", np.max(df['Investment_Amount_USD']))
print("Min Investment:", np.min(df['Investment_Amount_USD']))
print("Std Investment:", np.std(df['Investment_Amount_USD']))

# 9. Pandas Operations
print("\nValue Counts:")
print(df['Industry'].value_counts())

# 10. Visualization 1 - Industry Count
sns.countplot(data=df, x='Industry')
plt.title('Startup Count by Industry')
plt.xticks(rotation=45)
plt.show()

# 11. Visualization 2 - Investment Distribution
sns.histplot(data=df, x='Investment_Amount_USD', bins=30)
plt.title('Investment Amount Distribution')
plt.show()

# 12. Visualization 3 - Box Plot
sns.boxplot(data=df, x='Industry', y='Investment_Amount_USD')
plt.title('Investment by Industry')
plt.xticks(rotation=45)
plt.show()

# 13. Groupby Operation
print("\nAverage Investment by Industry:")
df.groupby('Industry')['Investment_Amount_USD'].mean()
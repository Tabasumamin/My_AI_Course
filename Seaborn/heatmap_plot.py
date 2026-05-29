import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("My-Ai-Course/RealEstate-USA.csv")

# Only numeric columns (important for heatmap)
numeric_df = df.select_dtypes(include=['number'])

# Correlation matrix
corr = numeric_df.corr()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)

plt.title("Real Estate Correlation Heatmap")
plt.show()
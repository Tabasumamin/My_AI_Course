import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("My-Ai-Course/RealEstate-USA.csv")

# Boxplot city vs price
sns.boxplot(x=df["city"], y=df["price"])

plt.xticks(rotation=45)
plt.title("City vs Price")
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("My-Ai-Course/RealEstate-USA.csv")

# Relationship between price and house size
sns.scatterplot(x=df["house_size"], y=df["price"])

plt.title("Price vs House Size")
plt.show()


# Relationship between beds and price
sns.scatterplot(x=df["bed"], y=df["price"])

plt.title("Beds vs Price")
plt.show()
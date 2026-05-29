import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("RealEstate-USA.csv")

# Price distribution
sns.histplot(df["price"], kde=True)

plt.title("Price Distribution")
plt.show()


# House size distribution
sns.histplot(df["house_size"], kde=True)

plt.title("House Size Distribution")
plt.show()
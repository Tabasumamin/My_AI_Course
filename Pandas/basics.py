import pandas as pd

df = pd.read_csv("RealEstate-USA.csv")

print(df)

print("Data types:", df.dtypes)

print("Info:")
df.info()

print("Last three rows:")
print(df.tail(3))

print("First three rows:")
print(df.head(3))

print("Describe:")
print(df.describe())

print("Shape:", df.shape)
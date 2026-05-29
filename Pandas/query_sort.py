import pandas as pd

df = pd.read_csv("RealEstate-USA.csv")

# query
selected_rows = df.query("bed > 3")
print(selected_rows)

print(len(selected_rows))

# sort by price
sorted_df = df.sort_values(by='price')
print(sorted_df)

# sort by multiple columns
df1 = df.sort_values(by=['price', 'zip_code'])
print(df1)
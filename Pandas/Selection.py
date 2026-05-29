import pandas as pd

df = pd.read_csv("RealEstate-USA.csv")

# single column
city = df['city']
print(city)

# multiple columns
print(df[['city', 'house_size']])

# loc - single row
print(df.loc[1])

# loc - multiple rows
print(df.loc[[1, 3]])

# loc - slice rows
print(df.loc[1:5])

# condition
print(df.loc[df['city'] == 'Gateway Properties'])

# loc single column
print(df.loc[:1, 'city'])

# loc multiple columns
print(df.loc[:1, ['city', 'house_size']])
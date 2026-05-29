import pandas as pd

df_index_col = pd.read_csv(
    'RealEstate-USA.csv',
    index_col='zip_code'
)

# single row
print(df_index_col.iloc[0])

# multiple rows
print(df_index_col.iloc[[1, 3, 5]])

# slice rows
print(df_index_col.iloc[2:5])

# single column
print(df_index_col.iloc[:, 2])

# multiple columns
print(df_index_col.iloc[:, [2, 4]])

# slice columns
print(df_index_col.iloc[:, 2:4])

# combined
print(df_index_col.iloc[[1, 3, 5], 2:4])
import pandas as pd

df_index_col = pd.read_csv(
    'RealEstate-USA.csv',
    index_col='zip_code'
)

print(df_index_col)

print(df_index_col.dtypes)

df_index_col.info()

# single row by index
print(df_index_col.loc[601])

# condition
print(df_index_col.loc[df_index_col['city'] == 'Gateway Properties'])
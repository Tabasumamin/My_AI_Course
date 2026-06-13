import pandas as pd 

df = pd.read_csv("FastFoodRestaurants.csv" ,delimiter=',')

print(df)

print("df - data types :" , df.dtypes)

df.info()

print("Last three rows:")

print(df.tail(3))

print()

print("First three rows:")

print(df.head(3))

print()

#Summary of Statistics of DataFrame using describe() method.

print('Summary of Statistics of DataFrame using describe() method:' , df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.

print("Counting the rows and columns in Dataframe using shape():" , df.shape)

print()

print(df.isnull().sum())

print(df.duplicated().sum())

# access the column province
province = df['province']
print("access the province column: df : ")
print(province)
print()

# Access the multiple columns

latitude_longitude = df[["latitude" , "longitude"]]
print("access multiple columns: df : ")
print(latitude_longitude)
print()

#Selecting a single row using .loc
row = df.loc[1]
print("Selecting a single row using .loc")
print(row)
print()

#Selecting multiple row using .loc
row1 = df.loc[[1,4]]
print("Selecting a multiple row using .loc")
print(row1)
print()
#Selecting a slice of rows using .loc
row3 = df.loc[1:5]
print('Selecting a slice of rows using .loc')
print(row3)
print()

#Conditional selection of rows using .loc
row4 = df.loc[df['name'] == "McDonald's"] 
print("Conditional selection of rows using .loc")
print(row4)
print()

#Selecting a single column using .loc
row5 = df.loc[:6,"name"]
print('Selecting a single column using .loc')
print(row5)
print()

#Selecting multiple columns using .loc
row6 = df.loc[:6,['city','province']]
print("Selecting multiple columns using .loc")
print(row6)
print()

#Selecting a slice of columns using .loc
row7 = df.loc[:4,'country':'province']
print("Selecting a slice of columns using .loc")
print(row7)
print()

#Combined row and column selection using .loc
row8 = df.loc[df['name'] == "McDonald's",'latitude':'province']
print("#Combined row and column selection using .loc")
print(row8)
print()

print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here

df_index_col = pd.read_csv('FastFoodRestaurants.csv' , index_col = 'keys')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

# Second cycle - with index_col as key

#Selecting a single row using .loc
row9 = df_index_col.loc["us/oh/washingtoncourthouse/530clintonave/-791445730"]
print("#Selecting a single row using .loc")
print(row9)
print()


#Selecting multiple rows using .loc
row10 = df_index_col.loc[["us/oh/washingtoncourthouse/530clintonave/-791445730", "us/ny/massena/6098statehighway37/-1161002137"]]
print("#Selecting multiple rows using .loc")
print(row10)
print()

#Selecting a slice of rows using .loc
row11 = df_index_col.loc["us/ny/massena/324mainst/-1161002137":"us/ny/massena/6098statehighway37/-1161002137"]
print("#Selecting a slice of rows using .loc")
print(row11)
print()

#Conditional selection of rows using .loc
row12 = df_index_col.loc[df_index_col['name'] == "McDonald's"]
print("#Conditional selection of rows using .loc")
print(row12)
print()


#Selecting a single column using .loc
row13 = df_index_col.loc[:"us/oh/athens/139columbusrd/990890980",'name']
print("#Selecting a single column using .loc")
print(row13)
print()

#Selecting multiple columns using .loc
row14 = df_index_col.loc[:"us/oh/athens/139columbusrd/990890980",['postalCode','province']]
print("#Selecting multiple columns using .loc")
print(row13)
print()

#Selecting a slice of columns using .loc
row14 = df_index_col.loc[:"us/oh/athens/139columbusrd/990890980",'postalCode':'province']
print("#Selecting a slice of columns using .loc")
print(row14)
print()

#Combined row and column selection using .loc
row15 = df_index_col.loc[df_index_col['name'] == '"us/oh/athens/139columbusrd/990890980"','postalCode':'province']
print("#Combined row and column selection using .loc")
print(row15)
print()


#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()
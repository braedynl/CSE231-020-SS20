# pandas is typically imported with the name "pd"
# since the word "pandas" is too cumbersome
import pandas as pd

# Creating a DataFrame() from default Python types
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
            'age': [42, 52, 36, 24, 73], 
            'preTestScore': [4, 24, 31, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70]
            }

# By default, pandas will set the column (and row) names to be numeric, i.e. 0, 1, 2, ...
# We, however, want the column names to be the keys of raw_data,
# so we take advantage of the `columns` parameter and `.keys()`
df = pd.DataFrame(raw_data, columns=raw_data.keys())

# Variables that are holding a DataFrame() instance are conventionally
# named `df`
print(df)
input()


# Types / Subset Data Frames

# This will get you back the Series() object at the column named "last_name"
print(df["last_name"])
print(type(df["last_name"]))

# While THIS will get you back a whole new DataFrame() object solely comprised
# of the column named "last_name"
print( df[ ["last_name"] ] )
print(type(df[["last_name"]]))

# You can build up new DataFrame() objects from subsets of another like this.
# Here, we're extracting the "last_name" column and the "age" column
print( df[ ["last_name", "age"] ] )


# If you want to change the row names, we can set one of the columns to act
# as the row names instead (there's also an `index` parameter option when
# you initialize a DataFrame() instance)

# We can simply call the column name! (Case-sensitive)

df.set_index('last_name', inplace=True) # `inplace` means to change the df... in-place. (Like .sort() on a list)
print(df)
input()

# Access the values by calling them by their name, or by their position in the index or column

# The order of access, (in both of the upcoming methods), is always, always, ALWAYS:
# row, column
# [row][column]
# row -> column

# However you're accessing ANYTHING with respect to pandas, it's always ROW, COLUMN


# `loc` is short for "locate"
# `iloc` specifies that you're going to access by INDEX, hence the name `i` + `loc`
# `loc` specifies that you're going to access by NAME, hence just `loc`

# You'll notice that these method functions use the bracket notation

# `iloc[]` uses INDICES

# iloc[0] -> Row access: [Jason, 42, 4, 25]
# iloc[0][0] -> Column access: [Jason] 

print('Value at position [0,0]: ', df.iloc[0][0])

# while `loc[]` uses NAMES

# loc["Ali"] -> Row access: [Tina, 36, 31, 57]
# loc["Ali"]["age"] -> Column access: [36]

print('The age of the person with last name Ali: ', df.loc['Ali']['age'])

input()


# Row and Column Selection

# iloc[ ROW_START_INDEX:ROW_END_INDEX , COL_START_INDEX:COL_END_INDEX ]
# loc[ ROW_START_NAME:ROW_END_NAME , COL_START_NAME:COL_END_NAME ]

# Remember that with splicing, you can leave a parameter empty to
# specify that you want the remaining items in that row/column

# You can also state a single item to act as both the START and END
# point, effectively selecting everything in the entire row/column

# It might be helpful to think of `:` as meaning "to" in natural language,
# while `,` as meaning "and from"

# iloc[0,2:3]
# "Row 0 and from column 2 to column 3"

# loc["names":"grades", "average"]
# "Row 'names' to row 'grades' and from column 'average'"


# Use `iloc[]` to select row `0`
# iloc[ ROW_START_INDEX:ROW_END_INDEX , COL_START_INDEX:COL_END_INDEX ]

# df.iloc[0 , :]

# "Row 0 and from every column"

# ROW_START_INDEX -> 0
# ROW_END_INDEX -> 0
# COL_START_INDEX -> Not specified
# COL_END_INDEX -> Not specified

print(df.iloc[0,:])
input()


# Use `loc[]` to select column `age`
# loc[ ROW_START_NAME:ROW_END_NAME , COL_START_NAME:COL_END_NAME ]

# df.loc[: , "age"]

# "Every row and from column 'age'"

# ROW_START_NAME -> Not specified
# ROW_END_NAME -> Not specified
# COL_START_NAME -> "age"
# COL_END_NAME -> "age" 

print(df.loc[:,"age"])
input()


# loc[ ROW_START_NAME:ROW_END_NAME , COL_START_NAME:COL_END_NAME ]

# df.loc["Miller":"Jacobson", "age":"preTestScore"]

# "Row 'Miller' to row 'Jacobson' and from column 'age' to column 'preTestScore'"

# ROW_START_NAME -> "Miller"
# ROW_END_NAME -> "Jacobson"
# COL_START_NAME -> "age"
# COL_END_NAME -> "preTestScore"

print(df.loc["Miller":"Jacobson", "age":"preTestScore"])
input()


# Reading a CSV file

df = pd.read_csv('iris.csv') # This file has 150 rows and 5 columns

print('size of the file: ', df.shape)   # .shape will give you the dimensions of the df

print('Type of one column: ', type(df['species']))

print('Type of two columns: ', type(df[ ['sepal_width','species'] ] ))

input()


# Other Useful Methods

# Shows the first 5 rows in the DataFrame
print("First 5 rows of all columns:\n", df.head())
input()

# Shows the last 5 rows in the DataFrame 
print("last 5 rows of all columns:\n", df.tail())
input()

# Calculate mean of column 'sepal_length'
print("Mean of sepal length:\n", df['sepal_length'].mean())
input()

# There's also .max(), .min(), .mode(), .sum(), there's a lot
# https://pandas.pydata.org/pandas-docs/stable/reference/series.html


# Filtering

# You might want to think of this as saying:
# "Access the df, where in column 'species', the row contains 'setosa'"
#             df[              df['species']        ==        "setosa" ]

df_new = df[df['species'] == 'setosa']

print(df_new)

# ----- Read and Write Data

# importing pandas
import pandas as pd
# Reading to various files
df = pd.read_csv('data.csv')
df = pd.read_json('data.json')
df = pd.read_html('data.html')
df = pd.read_sql('yourDatabase.yourSQLtable')

# Writing to various files
df.to_csv('output.csv', index=False)
df.to_parquet('output.parquet')
df.to_xml('output.xml')

# ----- Data Exploration

# Display the first 5 (default) rows of the DataFrame.
df.head()
# Display the last 3 rows of the DataFrame.
df.tail(3)
# Generate descriptive statistics of the DataFrame.
df.describe()

# An example from the pandas documentation:
>>> df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
...                    'numeric': [1, 2, 3],
...                    'object': ['a', 'b', 'c']
...                   })
>>> df.describe()
       numeric
count      3.0
mean       2.0
std        1.0
min        1.0
25%        1.5
50%        2.0
75%        2.5
max        3.0

# ----- Creating dataFrames

# Passing in lists or Numpy array
data = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
# Passing in a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
# from a csv file (as shown above)
df = pd.read_csv('file.csv')

# ----- Selecting and Indexing

# select column 'age'
df['age']
# selecting a subset of [rows 2-4, columns 1 and 2] (to learn more search 'slicing')
df.iloc[2:5, 0:2]
# selecting by label [all rows, columns 'name' and 'age']
df.loc(:, ['name', 'age'])

# ----- Filtering

# filter rows where the age is greater than 25
df[df['age'] > 25]
# filter by population OR area (new dataframe from the world table/dataframe)
df = world[(world['population'] >= 25000000) | (world['area'] >= 300000)]
# filter products by low-fat AND recyclable (new dataframefrom the products table/dataframe)
df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]

# ----- Sorting, Grouping and De-duping

# sort dataframe by author_id in place (don't create a new dataframe)
df.sort_values(by=['author_id'], inplace=True)
# remove duplicate author_id values in place (don't create a new dataframe)
df.drop_duplicates(subset=['author_id'], inplace=True)
# Rank() computes numerical data ranks along an axis. using method='dense' 
# assigns the same rank to any tied scores in the data ensuring no skipped ranks and the same rank for tied scores
scores['rank'] = scores['score'].rank(method='dense', ascending=False)
# group users table by location
df = users.groupby('location')

# ----- String Methods

# filter tweets dataframe for values longer than 15 characters
df = tweets['content'].str.len() > 15
# Capitalize the first letter of the name column in the users table
users['name'] = users['name'].str.capitalize()
# convert string to lower or upper respectively
df['column'].str.lower()
df['column'].str.upper()
# replace occurences of a string with a new string
df['column'].str.replace('old_string', 'new_string')
# find which rows of the content column contains the standalone word 'bull' (not case sensitive) 
bulls = files['content'].str.contains(" bull ", case=False)
# remove leading and trailing whitespace
df['column'].str.strip()
# split strings on a delimiter (comma) into a list
df['column'].str.split(',')

# --- Joining

# left join the customers table with the orders table on customer.id == orders.customerId
# merge() is the most robust way to join as you can specify columns on which to join
df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
# Vertical concatenation
result = pd.concat([df1, df2], axis=0)
# joining two dataframes on the index (left join is default)
result = df1.join(df2, how='left')
# append() is used to append rows from one df to another
result = df1.append(df2)

# ----- Apply a function

# apply a function that sets the employee bonus column equal to salary if 
# their id is even and their name does not start with M, otherwise set bonus to 0
employees['bonus'] = employees.apply(
        lambda x: x['salary'] if x['employee_id'] % 2 and not x['name'].startswith('M') else 0, axis=1
    )

# Define a custom function, and...
def square_value(x):
    return x ** 2

# Apply the function to each element in the DataFrame
result = df.apply(square_value)

# ----- Math Operations

# absolute values
df['column'].abs()
# round to 2 decimals
df['column'].round(2)
# mean and median
df['column'].mean()
df['column'].median()
# clip values outside a range
df['column'].clip(lower, upper)
# Min and Max
df['column'].min()
df['column'].max()

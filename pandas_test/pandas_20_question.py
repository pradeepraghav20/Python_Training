# 4. How do you create a DataFrame from a CSV file in Pandas?

import pandas as pd
data=pd.read_csv("friends.csv")
print((type(data)))
print(data.head(1))

# 5. How do you select specific columns from a DataFrame in Pandas
# print(data[['name']])
# print(data[data.iloc[:0:2]]) #need clear
# print(data.head(2))
# print(data.tail(2))

# 7. How do you handle missing data in a DataFrame in Pandas?
print(data.isna())
print(data.isnull)

print(data.dropna())
print(data.to_string())
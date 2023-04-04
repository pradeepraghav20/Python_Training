import pandas as pd
import numpy as np

dict1={
    "name":['pradeep','raghav'],
    "marks":[22,33],
    "city":["delhi","noida"]
}
df=pd.DataFrame(dict1)
# df.to_csv("friends1.csv",index=False)
df.to_csv("friends1.csv")
df.index=['first','second']
# print(df)
#
# print (pd.read_csv('friend1.csv'))

# df.head(1)
# df.tail(1)
# print(df.describe())

# fri=pd.read_csv('friends.csv')
# fri['name'][0]="manish"

# fri.to_csv('friend1.csv')

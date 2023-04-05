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

newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(newdf)
# print(newdf.head())
# print(type(newdf))
# print(newdf.describe())
# print (newdf.index)
# print(newdf.columns)
# print(newdf.T)

print(newdf[0])
newdf2=newdf # view
newdf2=newdf.copy()
newdf.drop(0,axis=1)
print(newdf2)
#newdf.loc([0,1],[0,1])

# print(newdf)
# print(newdf.iloc[0,4])
#print(newdf.iloc[[0,1],[1,1]])
print(newdf.head())
print(newdf.drop(0))
print(newdf.head())




# newdf.drop(4)
# newdf[1]=None
# print(newdf.dropna())
#
# newdf[0]=None
# # print(newdf)
# print(newdf.fillna(120))
# print(newdf.duplicated())
# print(newdf.drop_duplicates())

import  os
print(os.getcwd())
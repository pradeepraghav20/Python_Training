# import numpy as np
# # arr=np.array([1,2,3,4,5])
# # arr2=np.array((1,2,3,5,6,6,7))
# # # print(arr2)
# # #print(arr.max())
# #
# # arr3=np.array([[1,2,3],[4,5,6]])
# #
# # arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# # #print(arr1)
# # # print(arr3)
# # print(arr1.dtype)
# # # print(arr1.ndim)
# # print(arr.shape)
# # print(arr.ctypes)
#
# #
# #
# # a = np.array([[1,2],[3,4],[5,6]])
# # a=a.reshape(2,3)
# # print(a.shape)
# # print(a)
# # # print(a)
#
#
# # a = np.array([[1,2],[3,4],[5,6]])
# # print("printing the original array..")
# # print(a)
# # a=a.reshape(2,3)
# # print("printing the reshaped array..")
# # print(a)
# #print (np.__version__)
#
# #Series
# import pandas as pd
#
# # a=[1,3,3,33,4]
# # res=pd.DataFrame(a)
# # print(res)
# #
# #
# # res=pd.DataFrame(a,index=('a','b','c','d','e'))
# # print(res)
#
#
# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df.loc[0])
import pandas as pd

# file=pd.read_csv("C:\Users\prade\Downloads\data.csv")
# print (file.to_string())

pd.options.display.max_rows=10
df = pd.read_csv('C:/Users/prade/Downloads/data.csv')

#print(df.to_string())

print(df.head(10))
print(df.info())





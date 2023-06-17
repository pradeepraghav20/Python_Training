import numpy as np
array1=np.array((3,3,3,3))
# print(array1)
# print(array1[0])


array2=np.array([[1,2,3],[4,5,6]])
# print(array2)
print(array2[0][1])


#copy and view

array1=np.array((range(10)))
print(array1)
copy_array=array1.copy()
print(copy_array)
view_array=array1.view()
print(view_array)


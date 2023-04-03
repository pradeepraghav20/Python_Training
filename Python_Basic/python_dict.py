# # # # # # #1. Write a Python script to add a key to a dictionary. Go to the editor
# # # # # # dict1={0: 10, 1: 20}
# # # # # # dict1[2]=30
# # # # # # # print(dict1)
# # # # # # #update add new element in dict
# # # # # # dict1.update({4:40,6:40})
# # # # # # print(dict1)
# # # # # #
# # # # # #
# # # # # # #2. Write a Python script to concatenate following dictionaries to create a new one.
# # # # # # # dict2={5:50}
# # # # # # # dict3={9:90}
# # # # # # # dict1.update(dict2)
# # # # # # # dict1.update(dict3)
# # # # # # # print(dict1)
# # # # # #
# # # # # # dic1={1:10, 2:20}
# # # # # # dic2={3:30, 4:40}
# # # # # # dic3={5:50,6:60}
# # # # # # dic4 = {}
# # # # # # for d in (dic1, dic2, dic3): dic4.update(d)
# # # # # # print(dic4)
# # # # #
# # # # # 4. Write a Python script to check whether a given key already exists in a dictionary. Go to the editor
# # # #
# # # #
# # # # dic1={1:10, 2:20}
# # # # key=1
# # # # if key in dic1:
# # # #     print("Yess,Present")
# # # # else:
# # # #     print("Not Present")
# # # #
# # # #
# # # # # 5. Write a Python program to iterate over dictionaries using for loops. Go to the editor
# # #
# # # dic1={1:10, 2:20}
# # # for k,v in dic1.items():
# # #     print(k,v)
# # #
# # #
# # # 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# #
# # n=int(input())
# # d={}
# # for i in range(1,n):
# #     d[i]=i*i
# #
# # print(d)
#
# 8. Write a Python script to merge two Python dictionaries. Go to the editor

dict1={0: 10, 1: 20}
dict2={3:30,5:50}

dict1.update(dict2)
print(dict1)


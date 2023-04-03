# Create a Set in Python

stu_id={3,4,4,543,4,4,4}
print(stu_id)

#empty set

empty_set=set()
print(type(empty_set))
empty_dict={}
print(type(empty_dict))

#setmethod
stu_id.add(500)
print(stu_id)
copy_stu=stu_id.copy()
print(copy_stu)
del_ele=stu_id.pop()
print(del_ele)
print(stu_id)
stu_id2={4,4,5,4,3,3,3}
print(stu_id2)

res=stu_id.difference(stu_id2)
print(res)

print(stu_id.intersection_update(stu_id2))

print(stu_id2.remove(5))



#2. Write a Python program to iteration over sets. Go to the editor
#
# for i in stu_id2:
#     print(i,end=" ")


setx = set(["green", "blue"])
sety = set(["blue", "yellow"])

print(setx.symmetric_difference(sety))
print(setx.intersection(sety))
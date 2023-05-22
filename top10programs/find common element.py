list1=[4,1,2,3,4]
list2=[0,]
common_element=[]
for i in list1:
    if i in list2:
        if common_element.count(i)<1:
            common_element.append(i)

print(common_element)






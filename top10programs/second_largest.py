list1=[1,2,3,4,5,6,64,4,4]

#method 1

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            temp=list1[i]
            list1[i],list1[j]=list1[j],temp

print(list1[-2])

#method 2
list1.sort()


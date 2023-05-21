#Mean

list1=[1,2,3,4,5,6,7,89,5]
print("Mean",sum(list1)/len(list1))
list2=[1,2,3,4,4,4,5,5,5]
print("Mean2=",sum(list2)/len(list2))

#Median
list1.sort()

if (len(list1)%2==0):
    m1=list1[len(list1)//2]
    m2=list1[len(list1)//2-1]
    median=(m1+m2)/2
else:
    median=list1[len(list1)//2]

print(median)

#Mode

list1=[4,4,4,4,33,4,3,3]
frequency={}
for i in list1:
    frequency.setdefault(i,0)
    frequency[i]+=1

# print(frequency)

frequent=max(frequency.values())

for i,j  in frequency.items():
    if (frequent==j):
        mode=i
print(mode)


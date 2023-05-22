def ascending_order(l):
    for i in range(0,len(l)):
        for j in  range(i+1,len(l)):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
            else:
                pass

    print(l)

ascending_order([4,4,3,3,3232,23,34,0])


a=10
b=44
temp=a
a=b
b=temp
print(a)
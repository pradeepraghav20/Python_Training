l=[1,2,3]

f=0
last=len(l)-1

while(f<last):
    temp=l[f]
    l[f]=l[last]
    l[last]=temp
    f+=1
    last-=1
print(l)


#second largest

def second_largest(l):
    # max_val=max(l)
    # l.remove(max_val)
    # print(max(l))
    pass



second_largest([3,4,5,5,5,5,5,453,3,90])
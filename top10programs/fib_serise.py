n=int(input())

f=0
s=1

if (n<=0):
    print("enter positive number")
elif (n==1):
    print(s)
else:
    c=0
    while(c!=n):
        new_val=f+s
        print(f)
        f=s
        s=new_val
        c+=1
n=int(input())
rev_num=0
new_num=0
while(n>0):
    temp=n%10
    new_num+=temp**3

    #rev_num=rev_num*10+temp
    n=n//10

print(new_num)

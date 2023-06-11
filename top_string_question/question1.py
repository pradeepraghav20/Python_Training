# Q1) WAP to input a string and print the frequency of the characters.
# I/O :  aabccy
# O/P :  a:2
#        b:1
#        c:2
#        y:1


string=input()
#method1
d={}
for i in string:
    d[i]=string.count(i)

#method 2
for i in range(97,129):
    count=0
    for k in string:
        if (chr(i)==k):
            count+=1
    if (count!=0):
        print(chr(i),count)

# Q2) WAP to input a string and print the character with highest occurrence.
#
# I/O : aabbccyyyy
# O/P : y:4

string=input()
d={}
for i in string:
    d[i]=string.count(i)

print(d)
print(max(d.values()))

freq_val={}

for i in string:
    count=1
    if i in freq_val:
        freq_val[i]=freq_val[i]+1
    else:

        freq_val[i]=1

print(max(freq_val,key=freq_val.get))
print(freq_val)
print(freq_val.get)

from collections import Counter

print(Counter(string))

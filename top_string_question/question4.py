# Q4) How to remove all duplicates from a given string?
# I/O:Javaxx
# O/P:Javx

string=input()
new_str=""
for i in string:
    if i not in new_str:
        new_str=new_str+i
print(new_str)

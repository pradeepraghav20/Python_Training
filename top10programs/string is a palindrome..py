s="raghav"
copy_ste=s
if (copy_ste==s[::-1]):
    print("Both are same")
else:
    print("Not same")
    
reversed(s)
print(s)
if (s==copy_ste):
    print("both are same")

rev_str=""
for i in range(len(s),0,-1):
    print(i)
    rev_str+=s[i-1]

print(rev_str)
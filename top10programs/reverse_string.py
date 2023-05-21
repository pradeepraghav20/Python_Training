s="pradeep raghav"
rev_str=""
for i in range(len(s),0,-1):
    rev_str+=s[i-1]

print(rev_str)

#method 2
rev_str=""
for i in s:
    rev_str=i+rev_str
print(rev_str)


# Python code to reverse a string
# using reversed()

# Function to reverse a string
def reverse(string):
	string = "".join(reversed(string))
	return string



def reverse(string):
    string = "".join(reversed(string))
    return string


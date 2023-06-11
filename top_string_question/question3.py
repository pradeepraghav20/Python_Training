# Q3) WAP to reverse every word of string in proper manner.
# I/O: this is my book
# O/P: siht si ym koob


s=input().split()
for i in s:
    print(i[::-1],end=" ")


list_t=[(),('pradep','raghav'),(),(3,3,3)]
for i in list_t:
    if (len(i)==0):
        list_t.remove(i)

print(list_t)

def remove_tuple(list_t):
    return  [list_t for i in list_t if len(i)>0 ]
list_t=[(),('pradep','raghav'),(),(3,3,3)]

remove_tuple(list_t)
list=[-1,1,-1,8]
duplicate_num=[]
#method 1
for i in list:
    if list.count(i)>1 and i not in duplicate_num:
        duplicate_num.append(i)

#method 2
rep_list=[]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if (list[i]==list[j] and list[i] not in rep_list):
            rep_list.append(list[i])

print(rep_list)



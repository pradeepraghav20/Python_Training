def largest_num(l):
    lar_num=l[0]
    for i in l:
        if lar_num<i:
            lar_num=i
    print(lar_num)

largest_num([3,5,6,75,-2])
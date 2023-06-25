def remove_empty(test_list):
    # for i in test_list:
    #     if type(i)  is list and len(i)==0:
    #         test_list.remove(i)
    out=[res for res in test_list if res!=[]]
    print(out)



test_list = [5, 6, [], 3, [], [], 9]
res=list(filter(None,test_list))
print(res)
remove_empty(test_list)
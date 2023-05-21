# *args and **kwargs

def teting (a,b,c,*d):
    print(len(d))
teting(10,3,3,4,4,4,4,4,4,4)

def new_testing(**kw):
    print(len(kw))


kw={'name':"pradeep"}
new_testing(**kw)

#
# def myFun(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s == %s" % (key, value))
# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')


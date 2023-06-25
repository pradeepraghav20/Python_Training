import threading
def cube(l):
    for i in l:
        print("Cube-",i**3)

def square(l):
    for i in l:
        print("Square-",i**2)

l=[4,4,3,2,5,6,6]
cube(l)
square(l)

t1=threading.Thread(target=cube(l))
t2=threading.Thread(target=square(l))

t1.start()
t2.start()



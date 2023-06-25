import multiprocessing

def cube(l):
    for i in l:
        print("Cube-",i**3)

def square(l):
    for i in l:
        print("Square-",i**2)



l=[4,4,3,3,3]
if __name__ == "__main__":

    m1=multiprocessing.Process(target=cube(l))
    m1.start()




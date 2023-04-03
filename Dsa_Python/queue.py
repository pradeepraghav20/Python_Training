queue=[]
def enque():
    val=int(input("Entet the value"))
    queue.append(val)
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        del_val=queue.pop(0)
        print(del_val)


def display():
    for i in queue:
        print(i,end=" ")

while(True):
    print("1->Add ,2->Pop,3->Display, 4->Exit()")
    ch=int(input("Enter your choice"))
    if (ch==1):
        enque()
    elif (ch==2):
        dequeue()
    elif(ch==3):
        display()
    elif(ch==4):
        exit()
    else:
        print("Invalid choice")


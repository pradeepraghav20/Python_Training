stack=[]
def push():
    if len(stack)==n:
        print("Stack is full")
    else:
        val = int(input("New Value"))
        stack.append(val)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        del_item = stack.pop()
        print("Deleted Item",del_item)

def top_element():
    if not stack:
        print("Stack is empyt")
    else:
        top_element=stack[-1]
        print(top_element)

def print_stack():
    print("Complete stack",stack)

n=int(input("Limit of stack"))
while (True):
    print("1->add,2->Pop,3->View,4->exit")
    ch=int(int(input("Enter your choice")))
    if (ch==1):
        push()
    elif(ch==2):
        pop()
    elif(ch==3):
        print_stack()
    elif(ch==4):
        exit()
    else:
        print("incorrect option")




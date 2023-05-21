# Basic Functions of todo list are:
#
# Add a new todo
# Delete a todo
# Complete a todo
# Show remaining todos
# Show statistics of todo


def add_new_task():
    print("New Taks added")

ch=int(input("Enter your choice..?"))
while(ch!=0):
    if (ch==1):
        add_new_task()
        break
    else:
        pass

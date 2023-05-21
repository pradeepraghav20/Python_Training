import  random
#First_Way
def number_guess(user_number):
    random_number=random.randrange(1,2)
    if (user_number==random_number):
        print("User Won")
    else:
        # print("System Number was",random_number)
        print("You Loose")

# user_num=int(input("Please Enter Your Number(1-10)"))

n=random.randrange(1,10)
guess=int(input("Enter Any Number...?"))

while(n!=guess):
    if (n<guess):
        print("Too High..")
        guess=int(input("Enter Number Again..?"))
    elif (n>guess):
        print("Too Low..")
        guess=int(input("Enter the number again..."))
    else:
        break

print("hurrah guessed it right !!")










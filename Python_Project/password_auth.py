import getpass
user_name_password={"praghav":"pradeep123","manish":"manish@2023"}
user_name=input("User-Name")

if user_name in user_name_password:
    password = input("Enter the password")
    for i in user_name_password.keys():
        if user_name==i:
            while password!=user_name_password.get(i):
                password=input("enter password")
            break
    print("Verified")
else:
    print("User Not Presernt Please try again")






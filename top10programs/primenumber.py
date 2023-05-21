def prime_num(num):
    if (num>1):
        for i in range(2,num//2):
            if (num%i==0):
                print("Number is not prime")
                break
        else:
            print("Number is prime",num)

prime_num(13)



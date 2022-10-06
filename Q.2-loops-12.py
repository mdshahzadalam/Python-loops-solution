#2. Write a python script to check whether a given number is Prime or not

n=int(input("Enter a number:-"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"prime")
            break
    else:
            print(n,"not prime")
else:
    print(n,"not prime")
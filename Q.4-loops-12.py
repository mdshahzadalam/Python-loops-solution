#4. Write a python script to print all Prime numbers between two given numbers (both
#   values inclusive)

n=int(input("Enter first number:-"))
m=int(input("Enter second number:-"))
for i in range(n,m+1):
    count=0
    for j in range(2,(i//2+1)):
        if(i%j==0):
            count+=1
            break
    if (count ==0 and i!=1):
        print(i)
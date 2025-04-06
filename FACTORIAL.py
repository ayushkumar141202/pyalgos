n=int(input("enter the number for factorial:"))
fact=1
if(n<0):
    print("factorial for -ve number doesn't exist")
elif(n==0):
    print("factorial for zero(0) is one(1)")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("the factorial of",n,"is",fact)
    

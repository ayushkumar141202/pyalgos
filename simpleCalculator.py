num1=float(input("Enter the first number: "))
op=input("choose operation(+,-,*,/):")
num2=float(input("Enter the second number: "))

if op=='+':
    print("Result is: ", num1+num2)
elif op=='-':
    print("Result is: ", num1-num2)
elif op=='*':
    print("Result is: ", num1*num2)
elif op=='/':
    if num2!=0:
        print("Result is: ", num1/num2)
else:
    print("Error: Division by 0!")
    
    

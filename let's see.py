n = int(input("Enter the number: "))

if n < 2:
    print("This is not a prime number")
else:
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            print("This is not a prime number")
            break  
    else: 
        print("This is a prime number")

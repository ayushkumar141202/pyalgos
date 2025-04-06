#prime number with for loop: -


number=int(input("ENTER A NUMBER TO CHECK, IT IS PRIME NUMBER OR NOT:  "))

print("\n")
print("-----------------------------------------------------------------------")

if(number>1):
    for num in range(2,number):

        if number%num==0:
            print(number,"is NOT a PRIME NUMBER !!")
            break

    else:
        print(number,"is a PRIME NUMBER. ")
        

else:
    print(number,"is NOT a PRIME NUMBER !!")







    
    

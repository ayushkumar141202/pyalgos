#Vasooli Bhai
Principal=int(input("enter the principal value=>"))
Rate=int(input("enter the rate=>"))
Time=int(input("enter the years=>"))
Simple_Interest=(Principal*Rate*Time/100)
payable_amount= (Simple_Interest+Principal)
print("Simple interest is", Simple_Interest)
print("Payable amount is", payable_amount)

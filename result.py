a=eval(input("Enter your total marks:"))
if (a>600):
    print("Marks are invalid")
else:
    b=a/600*100
    print("Percentage is",str(b)+"%")
    
if(90<b<100):
     print("First division with",str(b)+"%")
elif(80<b<90):
    print("Second division with",str(b)+"%")
elif(70<b<80):
    print("Third division with",str(b)+"%")
elif(37<b<70):
    print("Passed with",str(b)+"%")
elif(b<37):
    print("Failed with",str(b)+"%")
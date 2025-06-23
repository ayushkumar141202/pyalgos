def is_palindrome(s):
    return s==s[::-1]
string = input("Enter the word:")

if is_palindrome:
    print("This is a palindrome")
else:
    print ("This is not a palindome")

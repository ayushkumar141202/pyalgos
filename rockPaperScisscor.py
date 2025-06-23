import random
choices = ["rock","paper","scissors"]
print("Rock,Paper,Scissors Game!!")
while  True:
    user = input("Choose rock,paper or scissor(or 'quit' to stop):").lower()
    if  user == 'quit':
        print("Thanks for playing!")
        break 
    if user not in choices:
        print("Invalid Choice. Try again!")
        continue
    
    computer=random.choice(choices)
    print("Computer chose:", computer)
    if user==computer:
        print("It's a tie!")
    elif(user == "rock" and computer == "scissors") or\
        (user == "paper" and computer == "rock") or\
       (user =="Scissors" and computer == "paper"):
           print("You Win!!")
    else:
           print("You Lose")
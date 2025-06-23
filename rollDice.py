import random
def roll_dice():
    return random.randint(1,6)
print("Dice rolling simulator")
while True:
        roll= input("Roll the Dice?(yes/no):").lower()
        if roll=="yes":
            print("you rolled:", roll_dice())
        elif roll == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please type 'yes' or 'no'")
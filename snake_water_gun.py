import random


def game(comp, you):
    if (comp == you):
        return None
    elif (comp == 's'):
        if (you == 'w'):
            return False
        elif (you == 'g'):
            return True
    elif (comp == 'w'):
        if (you == 'g'):
            return False
        elif (you == 's'):
            return True
    elif (comp == 'g'):
        if (you == 's'):
            return False
        elif (you == 'w'):
            return True


a = print("Computer Turn: Snake(s) water(w) or Gun(g):  ")
randno = random.randint(1, 3)
if (randno == 1):
    comp = 's'
elif (randno == 2):
    comp = 'w'
elif (randno == 3):
    comp = 'g'
you = int(input("Players Turn: Snake(s) water(w) or Gun(g):  "))
if (you == 1):
    you = 's'
elif (you == 2):
    you = 'w'
elif (you == 3):
    you = 'g'
a = game(comp, you)

print(f"Computer chose {comp} ")
print(f"You chose {you} ")

if (a == None):
    print("Tie!")
elif (a):
    print("You won the game!!!")
else:
    print("You lost the game")

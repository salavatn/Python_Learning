import random

systemNumber = (random.randrange(1,1000))
print("Try to find my Number!")

def myGame():
    game = True
    while game:
        userNumber = int(input("New GAME1: Enter your number: "))

        if userNumber > systemNumber:
            print("Try min number")
        elif userNumber < systemNumber:
            print("Try max number")
        elif userNumber == systemNumber:
            print("Correct!")
            break
        else:
            print("You need enter the Number!")

myGame()
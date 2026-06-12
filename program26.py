from random import randint
for s in range(1,11):
    guessNumber = int(input("Enter your guess number between 1 to 10 : "))
    randomNumber = randint(1,10)
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was : ",randomNumber)
    
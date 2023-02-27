import random

def checkGuess(target, g) -> bool:
    guess = int(g)
    if target == guess:
        print("Good Job!")
        return True
    elif guess > target:
        print("Too Big!")
        return False
    elif guess < target :
        print("Too Small!")
        return False
    
while True:
    randomNumber = random.randint(0,100)
    while True:
        guess = input("Guess a number between 0 and 100: ")
        if checkGuess(randomNumber, guess):
            break;
    print()
    yesNoAns = input("Would you Like to play again? ".title()).lower()[0]

    if yesNoAns == 'y':
        pass
    else:
        break

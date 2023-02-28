import random

def checkGuess(target, g) -> bool:
    guess = int(g)
    if target == guess:
        print("\nGood Job!")
        return True
    elif guess > target:
        print("Too Big!")
        return False
    elif guess < target:
        print("Too Small!")
        return False
    
while True:
    randomNumber = random.randint(0,100)
    while True:
        guess = input("Guess a number between 0 and 100: ")
        try:
            if checkGuess(randomNumber, guess):
                break;
        except ValueError:
            print("\nThat was 100% not a number. Try again.\n")
    print()
    yesNoAns = input("Would you Like to play again? (y/n) ".title()).lower()[0]

    if yesNoAns == 'y':
        print()
        pass
    else:
        break

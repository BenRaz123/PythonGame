import random
import os
from stat import S_IREAD
from stat import S_IWUSR
from statistics import mean

if not os.path.exists(".data"):
    dataLogAppend = open(".data", "a")
    dataLogAppend.write("* DATALOG_FILE <️ DO NOT WRITE TO THIS FILE >️\n")
    dataLogAppend.close()
else:
    dataLogRead = open(".data", "r")
    numbers = [eval(i) for i in dataLogRead.readlines()[1::]]

    print(f"\nWelcome Back!\nIt took you on average {round(sum(numbers)/len(numbers))} guesses to win.\nYour High score is {sorted(numbers, reverse=False)[0]}.\n")

os.chmod(".data", S_IREAD)
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
    numberOfGuesses = 1
    while True:
        guess = input("Guess a number between 0 and 100: ")
        try:
            if checkGuess(randomNumber, guess):
                break
            numberOfGuesses += 1
        except ValueError:
            print("\nThat was 100% not a number. Try again.\n")
    os.chmod(".data", S_IWUSR)
    dataLogAppend = open(".data", "a")
    dataLogAppend.write(f"{numberOfGuesses}\n")
    dataLogAppend.close()
    os.chmod(".data", S_IREAD)

    print(f"You won in {numberOfGuesses} guess{'es' if numberOfGuesses > 1 else ''}.\n")
    yesNoAns = input("Would you Like to play again? (y/n) ".title()).lower()[0]
    if yesNoAns == 'y':
        print()
        pass
    else: break
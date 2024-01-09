import random 

def askForGuess():
    while True:
        guess = input('> ')

        if guess.isDecimal():
            return int(guess)
        print('please enter a number between 1 and 100')

print('guess the number by inventwithpython')
print()
secretNumber = random.randint(1,100)

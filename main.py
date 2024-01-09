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
print('I am thinking of a number between 1 and 100')

for i in range(10):
    print('you have {} guesses left. Take a guess.'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break
        
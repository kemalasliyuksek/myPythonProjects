import random
randomNumber = random.randint(1,100)
print("-- NUMBER GUESSING GAME --")
print("\nA number between 1 and 100 was determined!")

process = 0

while True:
    try:
        guess = int(input('\nGuess the number : '))
        if guess == randomNumber:
            print('\nCONGRATULATIONS! You found it in', process, 'tries.')
            input('\nTo exit, press Q and press enter.  ').upper()
            break
        elif (guess > 100) or (guess < 0):
            print('\nPlease try with a number between 1 and 100')
        elif guess > randomNumber:
            process += 1
            print('\nYou should guess a SMALLER number. Attempts : ', process)
        elif guess < randomNumber:
            process += 1
            print('\nYou should guess a BIGGER number. Attempts : ', process)
        else:
            print('\nEnter a valid value!')
    except:
        print('\nEnter a valid value!')
'''Build a guessing game where the program generates a random number between 1 and 100. 
The user has to guess the number, and the program gives hints if the guess is too high or
 too low.'''
# remember how to generate random number
import random

random_input = random.randint(1,100)

while True:
    user_input = int(input('Enter any number between 1 to 100:'))
    
    if user_input== random_input:
        print('Hurraahh...!! You got it right.')
        break
    elif user_input > random_input:
        print('Guess a smaller number')
    else:
        print('guess grater number')
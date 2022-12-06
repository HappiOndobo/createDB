from random import randint

num = randint(1,10)
guess = eval(input('Enter your guess: '))
if guess == num:
    print('You got it!')
else:
    print('sorry. The number is ', num)
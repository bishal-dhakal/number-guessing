#guess random number problem
import random

def guess(x):
    random_num = random.randint(1,x)
    guess =0
    while guess!= random_num:
        guess= int(input(f'Guess a number between 1 and {x} :'))
        print(guess)
        if(guess<random_num):
            print('sorry,guess again.Too Low')
        elif guess > random_num:
            print('Sorry, guess again.TToo high.')

    print(f'hurray you have guessed the number {random_num} correctly ')

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !='c' :
        if low != high:
            guess= random.randint(low,high)
        else:
            guess= low
        feedback= input(f'Is {guess} too high(H), too low(L), or correct (C)??').lower()
        if feedback =='h':
            high = guess-1
        elif feedback=='l':
            low= guess+1

    print(f'hurray The computer guesses your number,{guess},correctly!')

computer_guess(10)
guess(10)


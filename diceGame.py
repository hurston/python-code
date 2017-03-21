"""Dice game that
does some stuff"""

from random import randint #imports randint to get a random number
from time import sleep

def get_user_guess():
    user_guess = int(raw_input("Enter a guess: "))
    return user_guess
  
def roll_dice(number_of_sides):
    first_roll = randint(1,number_of_sides)
    second_roll = randint(1,number_of_sides)
    max_val = number_of_sides * 2
    print "The maximum roll is %s" % (str(max_val))
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print "Wrong! You guessed a number higher than the maximum value. I already told you what that dang maximum value was. It was %s" % (str(max_val))
        return
    else:
        print "Rolling..."
        sleep(2)
        print "First Roll: %d" % (first_roll)
        sleep(1)
        print "Second Roll: %d" % (second_roll)
        total_roll = first_roll + second_roll
        print "Total Roll: %d" % (total_roll)
        print "Result..."
        sleep(1)
        if user_guess > total_roll:
            print "You won!!!"
            return
        else:
            print "You're a loser!!"
            return
roll_dice(8)
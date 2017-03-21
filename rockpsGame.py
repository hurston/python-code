"""Rock, Paper, Scissors Game
The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is
"""

from random import randint
from time import sleep 

OPTIONS = ["R","P","S"]
LOSE_MSG = "You lost you big fat loser!"
WIN_MSG = "Luck SOB, you won this time..."

def decide_winner(user_choice, computer_choice):
  print str(user_choice)
  print "Computer selecting..."
  sleep(1)
  print str(computer_choice)
  user_choice_index = OPTIONS.index(user_choice)
  computer_choice_index = OPTIONS.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice == "R" and computer_choice == "S":
      print WIN_MSG
  elif user_choice == "P" and computer_choice == "R":
      print WIN_MSG
  elif user_choice == "S" and computer_choice == "P":
      print WIN_MSG
  elif user_choice_index > 2:
      print "Invalid Choice!"
      return
  else:
    print LOSE_MSG

def play_RPS():
  print "Rock, Paper, Scissors Game!"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = OPTIONS[randint(0,len(OPTIONS)-1)]
  decide_winner(user_choice,computer_choice)

play_RPS()  

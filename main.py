#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print("Welcome to the game user\n")
choice = input("Would you like to choose the 'easy' or 'hard' mode?\n")
if choice == "easy":
  attempts = 10
else:
  attempts = 5

num = random.randint(0,100)

endgame = False
while endgame ==False:
  print(f"You have {attempts} attempts remaining left:\n")
  user = int(input("Make a guess: "))
  if user == num:
    print("Congrats, you guessed right!")
    endgame = True
  elif user<num:
    print("Too low\n")
    attempts-=1
  elif user>num:
    print("Too high\n")
    attempts-=1

  if attempts == 0:
    print("Game over, you lost")
    print(f"Answer is {num}\n")
    endgame = True
    

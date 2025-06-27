import random
ROCK ='''  
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER='''  
   _______
---'    ____)____
           ______)
          _________)
         ___________)
         __________)
---.____________)
'''

SCISSORS=''' 
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
 '''
game_ascii=[ROCK, PAPER, SCISSORS]

RANDOM_CHOICE =  random.randint(0, 2)
user= int (input("Enter your choice (ROCK, PAPER, SCISSORS): ")) #index 

if user == RANDOM_CHOICE:
    print (f"You chose {game_ascii[user]}.")
    print (f"computr chose {game_ascii[RANDOM_CHOICE]}.")
    print("It's a tie!")
# elif (user == ROCK and RANDOM_CHOICE == SCISSORS) or (user==PAPER and RANDOM_CHOICE == ROCK) or (user == SCISSORS and RANDOM_CHOICE == PAPER):
#     print (f"You chose {user}.")
#     print (f"computr chose {RANDOM_CHOICE}.")
#     print(f"You win! ")
elif (user == 0 and RANDOM_CHOICE == 2) or (user == 1 and RANDOM_CHOICE == 0) or (user == 2 and RANDOM_CHOICE == 1):
    print (f"You chose {game_ascii[user]}.")
    print (f"computr chose {game_ascii[RANDOM_CHOICE]}.")
    print(f"You win! ")
else:
    print (f"You chose {game_ascii[user]}.")
    print (f"computr chose {game_ascii[RANDOM_CHOICE]}.")
    print(f"You lose! ")
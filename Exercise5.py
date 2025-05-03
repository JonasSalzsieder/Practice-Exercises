import random


def random_number_within_range(lowest_number, highest_number):
  return random.randint(lowest_number, highest_number)

def get_user_choice():
  print("Please select a move. Rock, Paper, or Scissors!")
  user_choice =input("What do you choose?: ").capitalize()
  return user_choice

def get_computer_choice():  
    computer_guess = random_number_within_range(1,3)
    if computer_guess == 1:
       computer_guess_word = "Rock"
    elif computer_guess == 2:
       computer_guess_word = "Paper"
    else:
       computer_guess_word = "Scissors"
    return computer_guess_word

#Game
user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(computer_choice)

if user_choice == "Rock" and computer_choice == "Scissors":
   print("Congrats, you won!")
elif user_choice == "Paper" and computer_choice == "Rock":
   print("Congrats, you won!")
elif user_choice == "Scissors" and computer_choice == "Paper":
   print("Congrats, you won!")
elif user_choice == computer_choice:
   print("Too bad, it's a draw")
else:
   print("Unfortunate, you lost")
       


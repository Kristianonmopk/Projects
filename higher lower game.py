import os
import random
import art
from game_data import data


#display the logo
print(art.logo)


#create a count of user's score to keep track of their winning streak
count = 0


#compare A choice - which is randomly imported from game_data.py
choice_a = random.choice(data)
print(f"Compare A: {choice_a['name']}, {choice_a['description']}, {choice_a['country']}")
#display VS art
print(art.vs)



while True:
  
  #Against B choice - which is randomly imported from game_data.py
  choice_b = random.choice(data)
  
  print(f"Against B: {choice_b['name']}, {choice_b['description']}, {choice_b['country']}")
  #Get user input of which choice they choose
  user_choice = input("Who has more followers? Type 'A' or 'B': ")

  acceptable_inputs_a = ["A", "a"]
  acceptable_inputs_b = ["B", "b"]
  while user_choice not in acceptable_inputs_a and user_choice not in acceptable_inputs_b:
    user_choice = input("Please enter either choice 'A' or choice 'B'': ")

#Decide whether the user was correct or not - it is correct if the player guesses the choice with the higher following or if they have the same number in following they also pass
  if (choice_a['follower_count'] >= choice_b['follower_count'] and user_choice in acceptable_inputs_a) or (choice_b['follower_count'] >= choice_a['follower_count'] and user_choice in acceptable_inputs_b):
    #Add 1 to user's score if they were correct
    count += 1
    os.system('clear')
    print(art.logo)
    print(f"You're right! Current score: {count}")
    correct_choice = user_choice.lower()
    temporary_choice = 'choice_' + correct_choice
    if temporary_choice[7] == 'a':
      choice_a = choice_a
    elif temporary_choice[7] == 'b':
      choice_a = choice_b
    print(f"Compare A: {choice_a['name']}, {choice_a['description']}, {choice_a['country']}")
    print(art.vs)
  #End if user was wrong with ending message and reset score to 0
  else:
    os.system('clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {count}")
    count = 0
    break

  #Continue if the user was correct by keeping option they chose as the new choice 'a' and comparing against the random new choice 'b'

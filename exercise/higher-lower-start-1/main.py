from game_data import data
from art import logo, vs
import random
from replit import clear

GAME_ON = True
SCORE = 0


def generate_random_selector():
  return random.choice(data)


def win_or_loss(selector1, selector2):
  """Takes inputs as data to compare
     Return results of the comparison   
  """
  if selector1["follower_count"] > selector2["follower_count"]:
    return "A"
  else:
    return "B"


def game_on(selector_1, selector_2):
  """ Starts the game and continues till user enters incorrect answer
  """

  global SCORE
  print(logo)

  print(f"Compare A: {selector_1['name']}, {selector_1['description']}, from {selector_1['country']}")

  print(vs)

  print(f"Against B: {selector_2['name']}, {selector_2['description']}, from {selector_2['country']}")

  user_input = input("Who has more followers? Type 'A' or 'B' : ")
  result = win_or_loss(selector_1, selector_2)
  clear()
  
  if result == user_input:
    SCORE += 1
    print(f"You are right! Current score is : {SCORE}")
    if result == "A":
      game_on(selector_1, generate_random_selector())
    else:
      game_on(selector_2, generate_random_selector())
  else:
    print(f"Sorry, that's wrong. Final score is : {SCORE}")


selector_1 = generate_random_selector()
selector_2 = generate_random_selector()

if selector_1 == selector_2:
  selector_2 = generate_random_selector()

game_on(selector_1, selector_2)

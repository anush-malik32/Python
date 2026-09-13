total_matches = 10
players_score = 0
computers_score = 0
while total_matches>0:
  players_choice = input("Pick your choice between rock, paper, or scissors:").strip().capitalize()
  import random

  choices = ['Rock', 'Paper', 'Scissors']
  computers_choice = random.choice(choices)
  print(computers_choice)
  if players_choice == "Rock":
    if computers_choice == "Paper":
      print("Winner is computer")
      computers_score = computers_score + 1
    elif computers_choice == "Rock":
      print("tie")
    elif computers_choice == "Scissors":
      print("Winner is player")
      players_score = players_score + 1

  if players_choice == "Paper":
    if computers_choice == "Scissors":
      print("Winner is computer")
      computers_score = computers_score + 1
    elif computers_choice == "Paper":
      print("tie")
    elif computers_choice == "Rock":
      print("Winner is player")
      players_score = players_score + 1

  if players_choice == "Scissors":
    if computers_choice == "Rock":
      print("Winner is computer")
      computers_score = computers_score + 1
    elif computers_choice == "Scissors":
      print("tie")
    elif computers_choice == "Paper":
      print("Winner is player")
      players_score = players_score + 1

  total_matches = total_matches - 1


if computers_score > players_score:
  print("The winner of this round is computer! Better luck next time player.")
elif players_score > computers_score:
  print("The winner of this round is you player! Great job, you beat computer!")
elif players_score == computers_score:
  print("The winner of this round is player and computer. You guys both tied. Great job!")
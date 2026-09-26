import random

secret = random.randint(1,50)

attempts = 5

print("The computer has chosen a score between 1 and 50. You have 5 attempts to guess it!")

while attempts > 0:
  print(f"\nAttempts remaining: {attempts}")

  try:
    players_choice = int(input("Enter your guess:"))
  except ValueError:
    print("Please enter a valid number!")
    continue

  difference = abs(secret - players_choice)

  if difference == 0:
    print(f"🎉 Congratulations! You guessed the exact score: {secret}!")

  elif difference <= 5:
    print("🔥 Hot! You are incredibly close!")
  elif difference <= 15:
    print("☀️ Warm! You are getting closer.")
  elif difference <= 30:
    print("❄️ Cold. You are pretty far off.")
  else:
    print("🧊 Ice Cold! You are nowhere near it.")

  attempts -= 1


if attempts == 0:
  print(f"\nGame Over! You ran out of attempts. The computer's score was {secret}.")
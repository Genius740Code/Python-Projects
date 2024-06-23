import random

timesplayed = 0
Loses = 0
Wins = 0

# Function to save stats to a text file
def save_stats():
    with open("heads_or_tails_stats.txt", "w") as file:
        file.write(f"Times Played: {timesplayed}\n")
        file.write(f"Loses: {Loses}\n")
        file.write(f"Wins: {Wins}\n")

while True:
    user_input = input("Heads or Tails? (q to quit): ")

    if user_input.lower() == "q":
        break

    if user_input.lower() == "heads" or user_input.lower() == "tails":
        coin_flip = random.choice(["heads", "tails"])

        if coin_flip == user_input.lower():
            print("You win!")
            Wins += 1
        else:
            print("You lose!")
            Loses += 1

        timesplayed += 1
    else:
        print("Invalid input. Please enter 'Heads' or 'Tails'.")

# Display stats after the user decides to quit
print(f"\nFinal Stats:")
print(f"Times Played: {timesplayed}")
print(f"You lost {Loses} times.")
print(f"You won {Wins} times.")

# Save stats to a file
save_stats()

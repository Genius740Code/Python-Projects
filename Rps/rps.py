import random
import time

user_wins = 0
computer_wins = 0
times_played = 0
ties = 0

m = ["Rock", "Paper", "Scissors"]
r = ["r", "Rock", "rock"]
p = ["p", "Paper", "paper"]
s = ["s", "Scissors", "scissors"]

options = ["rock", "paper", "scissors"]

def read_score_from_file(file_path):
    global user_wins, computer_wins, ties, times_played
    try:
        with open(file_path, 'r') as file:
            scores = list(map(int, file.read().strip().split()))
            if len(scores) == 4:
                user_wins, computer_wins, ties, times_played = scores
            else:
                user_wins = computer_wins = ties = times_played = 0
    except FileNotFoundError:
        user_wins = computer_wins = ties = times_played = 0
    return user_wins, computer_wins, ties, times_played

def write_score_to_file(file_path, user_wins, computer_wins, ties, times_played):
    with open(file_path, 'w') as file:
        file.write(f"{user_wins} {computer_wins} {ties} {times_played}")

file_path = 'rps_scores.txt'
user_wins, computer_wins, ties, times_played = read_score_from_file(file_path)

print("Are you ready to play Rock, Paper, Scissors?")
time.sleep(0.5)

while True:
    User1 = input("Type Rock(r)/Paper(p)/Scissors(s) or Q to quit: ")
    computer_pick = random.choice(m)

    if User1.lower() == "q":
        break

    if User1 in r and computer_pick in r:
        print("Computer Chose", computer_pick,)
        print("It's a Tie")
        times_played += 1
        ties += 1

    elif User1 in p and computer_pick in p:
        print("Computer Chose", computer_pick,)
        print("It's a Tie")
        times_played += 1
        ties += 1

    elif User1 in s and computer_pick in s:
        print("Computer Chose", computer_pick,)
        print("It's a Tie")
        times_played += 1
        ties += 1

    elif User1 in r and computer_pick in p:
        print("Computer Chose", computer_pick,)
        print("Paper beats Rock")
        time.sleep(0.5)
        print("You Lose")
        computer_wins += 1
        times_played += 1

    elif User1 in r and computer_pick in s:
        print("Computer Chose", computer_pick,)
        print("Rock breaks Scissors")
        time.sleep(0.5)
        print("You Win")
        user_wins += 1
        times_played += 1

    elif User1 in p and computer_pick in r:
        print("Computer Chose", computer_pick,)
        print("Paper beats Rock")
        time.sleep(0.5)
        print("You Win")
        user_wins += 1
        times_played += 1

    elif User1 in p and computer_pick in s:
        print("Computer Chose", computer_pick,)
        print("Scissors Cut Paper")
        time.sleep(0.5)
        print("You Lose")
        computer_wins += 1
        times_played += 1

    elif User1 in s and computer_pick in r:
        print("Computer Chose", computer_pick,)
        print("Rock breaks Scissors")
        time.sleep(0.5)
        print("You Lose")
        computer_wins += 1
        times_played += 1

    elif User1 in s and computer_pick in p:
        print("Computer Chose", computer_pick,)
        print("Scissors Cut Paper")
        time.sleep(0.5)
        print("You Win")
        user_wins += 1
        times_played += 1

    else:
        print("Invalid Input")

    write_score_to_file(file_path, user_wins, computer_wins, ties, times_played)

print("Thanks for playing!\n")
print("You played", times_played, "times.")
print("You won", user_wins, "times.")
print("You lost", computer_wins, "times.")
print("You tied", ties, "times.")

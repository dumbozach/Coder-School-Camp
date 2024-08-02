import random

while True:
    cpu_choice = random.randint(1,3)
    user_choice = input("Do you choose rock, paper, or scissors")

    if cpu_choice == 1:
        cpu_choice = "rock"
    elif cpu_choice == 2:
        cpu_choice = "paper"
    else:
        cpu_choice = "scissors"

    if cpu_choice == "rock" and user_choice == "paper":
        print("You win!")
    elif cpu_choice == "paper" and user_choice == "scissors":
        print("You win!")
    elif cpu_choice == "scissors" and user_choice == "rock":
        print("You win!")

    if cpu_choice == "rock" and user_choice == "scissors":
        print("You lose! Try again")
    elif cpu_choice == "paper" and user_choice == "rock":
        print("You lose! Try again")
    elif cpu_choice == "scissors" and user_choice == "paper":
        print("You lose! Try again")
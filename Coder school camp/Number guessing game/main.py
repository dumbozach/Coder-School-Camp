import random
max = 100

difficulty = input("What difficulty would you like (Easy, Med, Hard)? The harder the difficulty, the more numbers you have to guess!")
if difficulty == "Easy":
    max = 10
    print("There are "+str(max)+" numbers that you can guess from!")
elif difficulty == "Med":
    max = 50
    print("There are "+str(max)+" numbers that you can guess from!")
elif difficulty == "Hard":
    max = 100
    print("There are "+str(max)+" numbers that you can guess from!")
else:
    print("That is not a valid difficulty!")

randnum = random.randint(1, max)
guesses = 0

while True:
    guess = input("What do you think the number is?")
    if int(guess) > randnum:
        print("That number is too high!")
        guesses += 1
    elif int(guess) < randnum:
        print("That number is too low!")
        guesses += 1
    else:
        guesses += 1
        print("Congrats! You guessed the number!")
        print("You took "+str(guesses)+" guesses!")
        break
balance = 0
while True:
    choice = input("Do you want to deposit, withdraw, or view your balance ")
    if choice == "Deposit":
        amountD = input("How much do you want to deposit?")
        balance += int(amountD)
        print("You have $"+str(balance))
    elif choice == "Withdraw":
        amountW = input("How much do you want to withdraw?")
        if int(amountW) > balance:
            print("You are too poor to do that")
        else:
            balance -= int(amountW)
            print("You have $"+str(balance))
    elif choice == "View":
        print("You have $"+str(balance))
    else:
        print("That is not a valid option")
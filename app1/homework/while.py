user_input = int(input("How many tasks do you complete?: "))
while user_input <= 5:
    if user_input < 5:
        print("You have to complete 5")
        break
    user_input = int(input("How many tasks do you complete?: "))

else:
    print("Take a break, you did more than 5")



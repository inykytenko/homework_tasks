counter = 0
wallet = 50
shelf = 80
bank = 100
card = 300

if wallet > 0 or shelf > 0 or bank > 0 or card:
    counter = counter + wallet + shelf + bank + card
else:
    print("No money")

print(counter)

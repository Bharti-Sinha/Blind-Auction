from replit import clear

from art import logo
print(logo)
print("Welcome to the silent auction program!")

biding = True
silent_auction = {}
while biding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  silent_auction[name] = bid

  more_bids = input("Are there more people in the room who want to bid? Type 'yes' or 'no'")

  if more_bids == 'yes':
    clear()

  else:
    biding = False
    highest = 0
    winner = ""
    print(silent_auction)
    for key in silent_auction:
      if silent_auction[key] > highest:
        highest = silent_auction[key]
        winner = key 
    print(f"The winner is {winner} with a bid of ${highest}.")


  

  



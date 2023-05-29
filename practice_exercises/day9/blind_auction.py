# from replit import clear
# from art import logo

# print(logo)
bidders = {}
keep_bidding = True

while keep_bidding:
  bidder = input("What is your name? ")
  bid = int(input("How much would you like to bid? $"))
  
  bidders[bidder] = bid
  
  more_bidders = input("Is there anyone else who would like to bid? Type 'yes' or 'no'.\n")

  # clear()

  if more_bidders == 'no':
    keep_bidding = False

    highest_bid = max(bidders.values())
    highest_bidder = max(bidders, key=bidders.get)
    
    print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")
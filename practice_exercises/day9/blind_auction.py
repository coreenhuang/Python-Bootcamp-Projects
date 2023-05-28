from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bidders = {}
keep_bidding = True

while keep_bidding:
  bidder = input("What is your name? ")
  bid = int(input("How much would you like to bid? $"))
  
  bidders[bidder] = bid
  
  print(bidders)
  
  more_bidders = input("Is there anyone else who would like to bid? Type 'yes' or 'no'.")
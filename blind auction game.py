import os
import art
print(art.logo)

#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction")

b_name = input("What is your name: ")

b_bid = input("What is your bid: ")

while b_bid.isdigit() == False:
  b_bid = input("What is your bid: ")

bids = {}
bids[b_name] = b_bid
b1_other_valid_responses_yes = ["Yes", "yes", "Y", "y"]
b1_other_valid_responses_no =  ["No", "no", "N", "n"]

b1_other = input("Are there any other bidders? Type 'Yes' or 'No': ") 

while b1_other not in b1_other_valid_responses_yes and b1_other not in b1_other_valid_responses_no:
  b1_other = input("Are there any other bidders? Type 'Yes' or 'No': ") 



os.system('clear')


#new page
while b1_other in b1_other_valid_responses_yes:
  
  b_name = input("What is your name: ")
  
  b_bid = input("What is your bid: ")
  while b_bid.isdigit() == False:
    b_bid = input("What is your bid: ")
  
  bids[b_name] = b_bid
  
  b1_other = input("Are there any other bidders? Type 'Yes' or 'No': ") 
  
  while b1_other not in b1_other_valid_responses_yes and b1_other not in b1_other_valid_responses_no:
    b1_other = input("Are there any other bidders? Type 'Yes' or 'No': ") 
    
  os.system('clear')
  
else:
  highest_bid = 0
  highest_bidder = ""
  for i, v in bids.items():
    if int(v) >= highest_bid:
      highest_bid = int(v)
      highest_bidder = i



#new page
print('The winner is ' + str(highest_bidder) + ' with a bid of ' + str(highest_bid))


from art import logo
import os
print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls||clear')


# from replit import clear
# from art import logo
# #HINT: You can call clear() to clear the output in the console.
# print(logo)
# data = {}
# should_continue = "yes"
# while should_continue == "yes":
#   name = input("What is your name?\n")
#   bid = int(input("What is your bid?\n"))
#   data[name] = bid

#   should_continue = input("Are there any other bidders. Type \'yes\' or \'no\'\n")
#   clear()

# max_value = 0
# for key, value in data.items():
#   if value > max_value:
#     max_value = value

# key_list = list(data.keys())
# val_list = list(data.values())

# pos = val_list.index(max_value)
# print(f"The highest bidder is {key_list[pos]} with a bid of {max_value}")

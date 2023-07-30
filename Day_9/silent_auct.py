from art import logo
print(logo)


should_end = False

auction_bids = {}

while not should_end:
    name = input("What is your name?\n")
    bid = input("How much would you like to bid?\n")
    bid = int(bid)

    auction_bids[name] = bid

    continue_bidding = input("Do you wish to end the bidding?\n")
    if continue_bidding == "yes":
        should_end = True

final_bid = 0
final_name = ""
for x in auction_bids.keys():
    if auction_bids[x] > 0:
        final_name = x
        final_bid = auction_bids[x]

print(f"The winner is {final_name} with a winning bid of ${final_bid}")
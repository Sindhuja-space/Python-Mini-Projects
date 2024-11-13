bids = {}

def find_highest_bidder(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        price = bids[bidder]
        if price > highest_bid:
            highest_bid = price
            winner = bidder
    print(f"The winner is {bidder} with amount of ${highest_bid}")

continue_bidding = True

while continue_bidding:

    name = input("What is your name?:  ")
    bid_amount = int(input("What is your bid amount?: $"))

    bids[name] = bid_amount

    should_continue = input("Type 'Yes' to continue or 'No' to exit:  ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        continue_bidding = True
    else:
        print("Enter valid input")





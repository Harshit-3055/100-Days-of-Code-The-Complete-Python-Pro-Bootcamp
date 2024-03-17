print("Welcome to Auction Program")
bidders = {}
anyotherbidder = "yes"
while anyotherbidder=="yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders.update({bid:name})
    anyotherbidder = input("Are there any other bidders? Type 'yes' or 'no'.")


allthevalues = bidders.keys()
winneramt = max(allthevalues)
winnername = bidders[winneramt]


print("The winner of the bid is ",winnername,"with a bid of $",winneramt)

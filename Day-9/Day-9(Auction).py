print("Welcome to Auction Program")
bidders = {}
anyotherbidder = "yes"
while anyotherbidder=="yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders.update({name:bid})
    anyotherbidder = input("Are there any other bidders? Type 'yes' or 'no'.")


print(bidders)
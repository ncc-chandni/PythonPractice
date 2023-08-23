print("Welcome to the secret auction program.")

auction_list = {}

end = False
while end == False:
  name = input("What is your name?: ")
  bid = int(input("What's your bid: $"))
  auction_list[name] = bid
  again = input("Are there any more bidders? yes or no:\n")
  if again == "no":
    end = True

print(auction_list)
i = 0
for name in auction_list:
  bid_amt = auction_list[name]
  if i < bid_amt:
    i = bid_amt
    winner = name
print(f"The highest bidder is {name} with bid amount ${i}") 
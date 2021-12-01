n = int(input())

winner_name = None
winner_bid = -1
for i in range(n):
    name = input()
    bid = int(input())
    if bid > winner_bid:
        winner_bid = bid
        winner_name = name

print(winner_name)

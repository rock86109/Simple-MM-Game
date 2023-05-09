## Market making game
import numpy as np
def buy_or_sell(sum_cards, ask, bid):
  if sum_cards > int(ask):
    return "Buy"
  elif sum_cards < int(bid):
    return "Sell"
  else:
    return "None"

cards = np.random.choice(52, size=9, replace=False) % 13 + 1
sum_cards = cards.sum()

position = 0
Loss = 0
bids = []
asks = []
round = 5
for i in range(round):
  print(f"No.{i+1} Interval: ")
  ask = input("Ask: ")
  bid = input("Bid: ")
  bids.append(bid)
  asks.append(ask)

  side = buy_or_sell(sum_cards, ask, bid)
  print(side)
  if side == "Buy":
    position -= 1
  elif side == "Sell":
    position += 1
  print(f"No.{i+1} Card: {cards[i]}")
  print("\n\n")


input("Enter to proceed.")
print(f"Position: {position}. Cards: {sum_cards}")



## expectation calculation practice
tmp = np.random.choice(52, size=9, replace=False) % 13 + 1
print(tmp)
input("")
sum(tmp)

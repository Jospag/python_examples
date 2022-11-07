import random

def unfair_coin_toss(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"

heads = 0
tails = 0

for trials in range(10000):
    if unfair_coin_toss(.7) == "heads":
        heads = heads + 1

    else:
        tails = tails + 1
print(f"Number of Heads is: {heads}")
print(f"Number of Heads is: {tails}")

ratio = heads / tails
print(f"The ratio of heads to tails is: {ratio}")
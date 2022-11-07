import random

def coin_flip():
    if random.randint(0,1) == 0:
        return "head"
    else:
        return "tail"

head_tally = 0
tail_tally = 0

for trials in range(10_000):
    if coin_flip() == "head":
        head_tally = head_tally + 1
    else:
        tail_tally = tail_tally + 1
print(f"Number of heads is: {head_tally}")
print(f"Number of tails is: {tail_tally}")
ratio = head_tally / tail_tally
print(f"The ratio of heads to tails is {ratio}")


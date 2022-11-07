import random

def run_regional_election(chance_A_wins):
    if random.random() < chance_A_wins:
        return "A"
    else:
        return "B"

def run_election(regional_chances):
    numb_of_regions_won_by_A = 0
    for chance_A_wins in regional_chances:
        if run_regional_election(chance_A_wins) == "A":
            numb_of_regions_won_by_A = numb_of_regions_won_by_A + 1

    numb_of_regions_won_by_B = len(regional_chances) - numb_of_regions_won_by_A
    if numb_of_regions_won_by_A > numb_of_regions_won_by_B:
        return "A"
    else:
        return "B"

CHANCES_A_WINS_REGION = [0.87, 0.65, 0.17]
num_trials = 10_000
num_times_A_wins = 0
for trials in range(num_trials):
    if run_election(CHANCES_A_WINS_REGION) == "A":
        num_times_A_wins = num_times_A_wins +1

print(f"Probability A wins: {num_times_A_wins / num_trials}")
print(f"Probability B wins: {1 - (num_times_A_wins / num_trials)}")
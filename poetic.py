import random

noun = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verb = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjective = [ "furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
preposition = [ "against", "after", "into", "beneath", "upon", "for", "in", "like",
                "over", "within"]
adverb = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def make_poem():
    no1 = random.choice(noun)
    no2 = random.choice(noun)
    no3 = random.choice(noun)

    while no1 == no2:
        no2 = random.choice(noun)
    while no1 == no3 or no2 == no3:
        no3 = random.choice(noun)
        
    v1 = random.choice(verb)
    v2 = random.choice(verb)
    v3 = random.choice(verb)
    
    while v1 == v2:
        v2 = random.choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = random.choice(verb)

    adj1 = random.choice(adjective)
    adj2 = random.choice(adjective)
    adj3 = random.choice(adjective)

    while adj1 == adj2:
        adj2 = random.choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjective)

    prep1 = random.choice(preposition)
    prep2 = random.choice(preposition)
    while prep1 == prep2:
        prep2 = random.choice(preposition)

    adv = random.choice(adverb)

    if "aeiou".find(adj1[0]) != -1:
        article = "An"
    else:
        article = "A"

    poem = (
        f"{article} {adj1} {no1}\n\n"
        f"{article} {adj1} {no1} {v1} {prep1} the {adj2} {no2}\n"
        f"{adv}, the {no1} {v2}\n"
        f"the {no2} {v3} {prep2} a {adj3} {no3}"
    )

    return poem


poem = make_poem()
print(poem)
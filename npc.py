import random
attacks = []
strength = []
durability = []
turn = []
hp = []
creature = ["Wolf", "Mutant spider", "Cyclops","Leviathan", "Yeti", "Gorgon", "Ghoul", "Minotaur"]
classes = ["Attacker","Defender","Speedster","All-Rounder", "Technical"]
cre = (random.choice(creature))
cla = (random.choice(classes))
if classes == "Attacker":
    hp = [10]
    strength = [15]
    durability = [10]
if classes == "Defender":
    hp = [15]
    strength = [10]
    durability = [15]
if classes == "Speedster":
    hp = [9]
    strength = [5]
    durability = [5]
if classes == "All-Rounder":
    hp = [13]
    strength = [12]
    durability = [12]
if classes == "Technical":
    hp = [11]
    strength = [10]
    durability  = [10]
print(f"A {cre} approaches, it's a {cla} type")

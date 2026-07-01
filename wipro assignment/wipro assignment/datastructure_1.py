import collections
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}


for person, fact in people_facts.items():
    print(f"{person}: {fact}")

print()

people_facts["Jeff"] = "Is afraid of heights."


people_facts["Jill"] = "Can hula dance."

for person, fact in people_facts.items():
    print(f"{person}: {fact}")
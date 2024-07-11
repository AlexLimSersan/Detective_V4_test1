import random
from itertools import combinations

def get_trait(trait, suspect):
    return suspect.get(random.choice(trait))


clue_categories = {
    "jacket_scrap": "jacket_type",
    "food_stain_jacket":"food_type",
    "drink_stain_jacket": "drink_type",
    "roach_alcv_food_stain":"food_type",
    "roach_alcv_drink_stain": "drink_type",
    "roach_roof_food_stain":  "food_type",
    "roach_roof_drink_stain": "drink_type",
    "spilled_drink":"drink_type",
    "broken_glass":"flask_type",
    "matches":"match_type",
    "spilled_cigs": "smoke_type",
    "roach_roof": "smoke_type",
    "roach_alcove": "smoke_type",
    "ashes_alcove": "smoke_type",
    "hair": "hair_type",
    "shoeprint": "shoe_type",
    "weapon_clues": "weapon_type",
    "fight_clues": "fight_type"
}

all_possible_traits = {}

mortician = {
    "jacket_type": ["suit", "leather"],
    "food_type": ["tomato","mustard", "grease", "pie"], #actually stain type; coffee only on jacket, no spill!
    "drink_type": ["coffee","whiskey", "red wine"],
    "match_type": ["old"],
    "smoke_type": ["tobacco","premium"],
    "hair_type": ["medium black"],
    "shoe_type": ["work boots","dress shoes"],
    "flask_type": ["flask"],
    "weapon_type":["knife","gun"],
    "fight_type": ["weak"],
}

gibbs = {
    "jacket_type": ["suit", "denim"],
    "food_type": ["mustard"],
    "drink_type": ["coffee","whiskey","rum", "white wine"],
    "match_type": ["new", "old"],
    "smoke_type": ["generic","premium"],
    "hair_type": ["bald"],
    "shoe_type": ["sneakers","dress shoes"],
    "flask_type": ["flask","glass"],
    "weapon_type":["knife","blunt"],
    "fight_type": ["strong"],
}


bertha = {
    "jacket_type": ["leather", "denim"],
    "food_type": ["tomato","grease","pie"],
    "drink_type": ["rum","white wine","red wine"],
    "match_type": ["new"],
    "smoke_type": ["generic","tobacco"],
    "hair_type": ["medium black"],
    "shoe_type": ["sneakers","work boots"],
    "flask_type": ["flask","glass"],
    "weapon_type":["knife","gun","blunt"],
    "fight_type": ["strong","weak"],
}

class Suspect:
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits

class Murderer(Suspect):
    def __init__(self, name, traits):
        randomized_traits = self.randomize(traits)
        super().__init__(name, randomized_traits)

    def randomize(self, traits):
        new_traits = {}
        for trait, possibilities in traits.items():
            new_traits[trait] = random.choice(possibilities)
        return new_traits


# Define the clues and their spawn frequencies

# Function to get the spawn frequency value (evaluate if it's a lambda)
clue_type_spawn_freq_dic = {
    "weapon_clues": 1,
    "fight_clues": 1,
    "jacket_scrap": 0.5,
    "shoeprint": 0.4,
    "spilled_drink": 0.3,
    "broken_glass": 0.3,
    "matches": 0.3,
    "spilled_cigs": 0.3,
    "roach_roof": 0.3,
    "roach_alcove": 0.3,
    "ashes_alcove": 0.3,
    "hair": 0.3,
    "food_stain_jacket": lambda clues, spawned: (spawned.get("jacket_scrap", 0) * 0.3),
    "drink_stain_jacket": lambda clues, spawned: (spawned.get("jacket_scrap", 0) * 0.3),
    "roach_alcv_food_stain": lambda clues, spawned: (spawned.get("roach_alcove", 0) * 0.3),
    "roach_alcv_drink_stain": lambda clues, spawned: (spawned.get("roach_alcove", 0) * 0.3),
    "roach_roof_food_stain":  lambda clues, spawned: (spawned.get("roach_roof", 0) * 0.3),
    "roach_roof_drink_stain":  lambda clues, spawned: (spawned.get("roach_roof", 0) * 0.3),
}
def get_spawn_frequency(clue_type, clues, spawned):
    if callable(clues[clue_type]):
        return clues[clue_type](clues, spawned)
    return clues[clue_type]

# Function to determine if a clue spawns based on its frequency
def does_spawn(frequency):
    return random.random() < frequency

# Calculate individual spawn probabilities and track spawned clues
spawned_clues = {}
spawn_probabilities = []


for clue_type in clue_type_spawn_freq_dic.keys():
    frequency = get_spawn_frequency(clue_type, clue_type_spawn_freq_dic, spawned_clues)
    spawn = does_spawn(frequency)
    spawned_clues[clue_type] = spawn
    spawn_probabilities.append(frequency)

# Function to calculate the probability of at least k clues spawning using dynamic programming
def probability_at_least_k_spawn(k, spawn_probs):
    n = len(spawn_probs)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: probability of 0 clues spawning is 1

    for prob in spawn_probs:
        for j in range(n, 0, -1):
            dp[j] = dp[j] * (1 - prob) + dp[j - 1] * prob
        dp[0] *= (1 - prob)

    total_prob = sum(dp[k:])
    return total_prob



mortician = Suspect("mortician", mortician)
gibbs = Suspect("gibbs", gibbs)
bertha = Suspect("bertha",bertha)

suspects = [bertha,gibbs,mortician]
# Find the murderer
murderer = random.choice(suspects)
assert murderer
murderer = Murderer(murderer.name, murderer.traits)


print(f"Spawned Clues")
for key, _value in spawned_clues.items():
    print(f"{key}: {_value}")

print(f"\n \nMURDERER: {murderer.name}")
for trait, value in murderer.traits.items():
    print(f"{trait}: {value}")



print(f"\n \n_____SCENARIO_____")

print(f"\nSPAWNED CLUES:")
for key, _value in spawned_clues.items():
    if _value:
        scenario_murder_trait = murderer.traits.get(clue_categories.get(key))
        print(f"- {key}: {scenario_murder_trait}")
print(f"__________")#Because of my personal interest in politics, and desire to positively contribute to Canada. I am excited to support the LPC in their mission to improve the lives of Canadians.

for key, _value in spawned_clues.items():
    if _value:
        scenario_murder_trait = murderer.traits.get(clue_categories.get(key))
        print(f"{key}: {scenario_murder_trait}")

        for suspect in suspects:
            if not isinstance(suspect, Murderer):
                for possibilities_by_trait in suspect.traits.values():
                    for possibility in possibilities_by_trait:
                        if possibility == scenario_murder_trait:
                            print(f"- {suspect.name} match: {possibility}")
        print(f"---")

shared_traits = []

#get all traits that the murderer has that are shared with suspect
for suspect in suspects:
    for possibilities_by_trait in suspect.traits.values():
        for possibility in possibilities_by_trait:
            for _ in murderer.traits.values():
                if _ == possibility:
                    shared_traits.append(_)

# try to see if you can identify murderer?
identify = {}
for trait in shared_traits:
    for suspect in suspects:
        for possibilities_by_trait in suspect.traits.values():
            for possibility in possibilities_by_trait:
                if trait == possibility:
                    already_present = identify.get(trait)
                    if already_present:
                        if suspect.name not in already_present:
                            identify[trait].append(f"{suspect.name}")

                    else:
                        identify[trait] = [suspect.name]



#print(murderer.name)
ordered_identify = {}
for key, value in identify.items():
    print(f"{key}: {value}")


for values in identify.values():
    if len(set(values)) == len(identify.values()):
        print(f"CANT IDENTIFY MURDERER, ALL CLUES from {murderer.name} MATCH {values} ")


count = 5
at_least_count = 7 #weapon and fight clues always spawn

# Calculate the probability of at least `value` clues spawning
prob_at_least_x = probability_at_least_k_spawn(count, spawn_probabilities)
prob_dont_spawn = 1 - probability_at_least_k_spawn(at_least_count, spawn_probabilities)

print(f"\nThe probability of at least {count} clues spawning is: %{prob_at_least_x*100:.1f}")

print(f"The probability of less than {at_least_count} clues spawning is: %{prob_dont_spawn*100:.1f}")


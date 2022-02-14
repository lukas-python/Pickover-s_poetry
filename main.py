import random


def a_or_an():
  
  """checking if first letter is constants"""
  
    if 'aeiouy'.find(choosen_adj[0][0]) != -1:
        return 'A'
    else:
        return 'An'

      
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]

adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]

adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

choosen_nouns = []
choosen_verbs = []
choosen_adj = []
choosen_prep = []

for word in range(3):
    random_noun = random.choice(nouns)
    choosen_nouns.append(random_noun)
    random_verb = random.choice(verbs)
    choosen_verbs.append(random_verb)
    random_adj = random.choice(adjectives)
    choosen_adj.append(random_adj)

for word in range(2):
    random_prep = random.choice(prepositions)
    choosen_prep.append(random_prep)

random_adv = random.choice(adverbs)

print(f"{a_or_an()} {choosen_adj[0]} {choosen_nouns[0]}")
print()
print(f"{a_or_an()} {choosen_adj[0]} {choosen_nouns[0]} {choosen_verbs[0]} {choosen_prep[0]} the {choosen_adj[1]} {choosen_nouns[1]}\n"
      f"{random_adv}, the {choosen_nouns[0]} {choosen_verbs[1]}\n"
      f"the {choosen_nouns[1]} {choosen_verbs[2]} {choosen_prep[1]} a {choosen_adj[2]} {choosen_nouns[2]}")




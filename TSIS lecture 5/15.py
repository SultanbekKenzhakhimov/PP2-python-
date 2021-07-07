import random
def rline(f):
    l = open(f).read().splitlines()
    return random.choice(l)
print(rline('b.txt'))
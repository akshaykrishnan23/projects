# Python program to read a random line from a file

import random
def random_line(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)
print(random_line("c.txt"))
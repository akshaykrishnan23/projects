# Python program to count the frequency of words in a file
from collections import Counter
fname="c.txt"
def word_count(fname):
        with open(fname,"r") as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("c.txt"))
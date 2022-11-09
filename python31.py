#python program to find the longest words

f="c.txt"
with open(f , "r") as fdata:
    wordsList = fdata.read().split()
longestWord= len(max(wordsList, key=len))
result = [tword for tword in wordsList if len(tword) == longestWord]
print("The longest words in this text file:")
print(result)
fdata.close()

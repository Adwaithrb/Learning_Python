word = input()
length = len(word)
first = word[:2]
last = word[length-2:]
star = (length - 4) * "*"
print(first+star+last)

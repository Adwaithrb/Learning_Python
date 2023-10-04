word = input()
num = int(input())
letter = input()

first = word[:num]
sec = word[num+1:]

new = first+letter+sec
print(new)
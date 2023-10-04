word = input()
num = int(input())

skip = word[:num]
last = word[num+1:]
print(skip+last)
word = input()
num = int(input())

length = len(word) - 3
res = word[length:]
print(res*num)
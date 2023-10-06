word_1 = input()
word_2 = input()
length = len(word_2)
diff = len(word_1) 
total = diff - length
new = word_1[total:]
check = word_2 == new
print(check)
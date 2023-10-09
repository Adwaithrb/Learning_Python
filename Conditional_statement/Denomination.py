amount = int(input())

no_of_100 = amount / 100
no_of_100 = int(no_of_100)
remaining = amount % 100

no_of_50 = remaining / 50 
no_of_50 = int(no_of_50)
remaining = remaining % 50

no_of_10 = remaining / 10 
no_of_10 = int(no_of_10)
remaining = remaining % 10

ones = remaining
print("100:"+str(no_of_100))
print("50:"+str(no_of_50))
print("10:"+str(no_of_10))
print("1:"+str(ones))
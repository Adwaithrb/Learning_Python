a = input()
b = input()

length = len(b)
slicing = a[:length]
length_of_slicing = len(slicing)
stars = "*" * length_of_slicing
second = a[length:]
print(stars+second)
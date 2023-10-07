one = input()
two = input()

con_1 = one[:3] == "DIS"
con_2 = two[:3] == "DIS"

if con_1 or con_2:
    print("Discount")
else:
    print("No Discount")
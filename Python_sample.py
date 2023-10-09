number = int(input())
if number < 50:
    charge = number * 2
elif number < 151:
    charge = (2 * 50) + (3 *(number - 50))
elif number < 250:
    charge = (2 * 50) + (3 * 100) +(5*(number - 150))
elif number <= 250:
    charge = (2 * 50) + (3 * 100) + (5 * 100) + (8 * (number - 250))
surcharge = charge * 0.2
print(float(surcharge+charge))
num = input()

a = num[0] 
b = num[1]
c = num[2]

seven = (int(a) > 7) and (int(b) > 7) and (int(c) > 7)

p_ab = int(a) * int(b) <= 30
p_bc = int(b) * int(c) <= 30
p_ac = int(a) * int(c) <= 30

res = p_ac and p_ab and p_bc
print(seven or res)
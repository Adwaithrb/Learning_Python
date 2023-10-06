first = int(input())
second = int(input())

sum_of_num = first + second
sum_of_num = str(sum_of_num)
sum_digit = len(sum_of_num) 
less = sum_digit < 3

prod = first * second
pro = str(prod)
pro_len = len(pro)
less_than = pro_len < 3

res = less_than and less
print(res)
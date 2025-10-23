def sum_of_divisors(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors

def is_perfect_number(n):
    return sum_of_divisors(n) == n

def is_abundant_number(n):
    return sum_of_divisors(n) > n

# Kiểm tra số hoàn thiện
n = int(input("Nhập một số nguyên dương: "))
if is_perfect_number(n):
    print(f"{n} là số hoàn thiện.")
else:
    print(f"{n} không phải là số hoàn thiện.")

# Kiểm tra số thịnh vượng
if is_abundant_number(n):
    print(f"{n} là số thịnh vượng.")
else:
    print(f"{n} không phải là số thịnh vượng.")\

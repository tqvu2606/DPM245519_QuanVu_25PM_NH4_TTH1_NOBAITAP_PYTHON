import math
def tinh_giai_thua(n):

    if n == 0:

        return 1

    return math.factorial(n)

def tinh_S(x, n):

    tong = x

    for i in range(1, n+1):

        tong += (x ** (2*i + 1)) / tinh_giai_thua(2*i + 1)

    return tong


x = float(input("Nhập giá trị của x: "))

n = int(input("Nhập giá trị của n: "))



ket_qua = tinh_S(x, n)

print(f"Giá trị của biểu thức S({x}, {n}) là: {ket_qua}")

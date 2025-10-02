import math



def Tinh_S(x,n):

    tong = 0

    for i in range(1, n+1):

        tong += (x**i)/math.factorial(i) #Hàm factorial của thư viện math hỗ trợ việc tính giai thừa của các số nguyên từ 1-i

    return tong





x = float(input("Nhập giá trị của x: "))

n = int(input("Nhập giá trị của n: "))



ket_qua = Tinh_S(x,n)

print(f"Giá trị của dãy số S({x},{n}) là: {ket_qua}")

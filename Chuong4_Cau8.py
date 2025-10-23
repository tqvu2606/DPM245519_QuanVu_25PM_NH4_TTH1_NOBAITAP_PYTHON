import math

def logarit(x, a):
    if x <= 0 or a <= 0 or a == 1:
        return "Xin lỗi, x và a phải lớn hơn 0 và a phải khác 1"
    else:
        return math.log(x) / math.log(a)

def main():
    x = float(input("Nhập giá trị x: "))
    a = float(input("Nhập cơ số a: "))
    
    result = logarit(x, a)
    print(f"log_{a}({x}) = {result}")

if __name__ == "__main__":
    main()

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def analyze_array(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    even_numbers = [num for num in arr if num % 2 == 0]
    prime_numbers = [num for num in arr if is_prime(num)]
    non_prime_numbers = [num for num in arr if not is_prime(num)]
    
    print("Dòng 1:", ", ".join(map(str, odd_numbers)), f"({len(odd_numbers)} số lẻ)")
    print("Dòng 2:", ", ".join(map(str, even_numbers)), f"({len(even_numbers)} số chẵn)")
    print("Dòng 3:", ", ".join(map(str, prime_numbers)))
    print("Dòng 4:", ", ".join(map(str, non_prime_numbers)))

# Nhập mảng số tự nhiên
arr = list(map(int, input("Nhập mảng số tự nhiên, cách nhau bởi dấu phẩy: ").split(',')))

# Phân tích và xuất thông tin
analyze_array(arr)

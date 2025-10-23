import random

def generate_unique_random_list(N):
    unique_numbers = set()  # Sử dụng set để đảm bảo các số không trùng nhau
    while len(unique_numbers) < N:
        unique_numbers.add(random.randint(1, 1000))  # Thay 1000 bằng giới hạn tùy ý của số ngẫu nhiên
    return list(unique_numbers)

N = int(input("Nhập số lượng số ngẫu nhiên bạn muốn tạo: "))
random_list = generate_unique_random_list(N)
print("List ngẫu nhiên không trùng nhau:", random_list

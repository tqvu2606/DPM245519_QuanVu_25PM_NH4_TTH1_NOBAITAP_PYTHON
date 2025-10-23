def count_characters(s):
    # Khởi tạo các biến đếm
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0
    space_count = 0
    vowel_count = 0
    consonant_count = 0

    # Tạo danh sách các nguyên âm và phụ âm
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    # Duyệt qua từng ký tự trong chuỗi
    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            special_count += 1

    # Xuất kết quả
    print("Số lượng chữ IN HOA:", uppercase_count)
    print("Số lượng chữ in thường:", lowercase_count)
    print("Số lượng chữ số:", digit_count)
    print("Số lượng ký tự đặc biệt:", special_count)
    print("Số lượng khoảng trắng:", space_count)
    print("Số lượng nguyên âm:", vowel_count)
    print("Số lượng phụ âm:", consonant_count)

# Nhập chuỗi từ người dùng
s = input("Nhập chuỗi: ")

# Gọi hàm và xuất kết quả
count_characters(s)

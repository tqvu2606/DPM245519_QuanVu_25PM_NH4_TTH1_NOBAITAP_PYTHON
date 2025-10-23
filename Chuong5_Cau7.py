def optimize_string(s):
    # Loại bỏ khoảng trắng dư thừa và chuyển đổi các từ thành viết hoa chữ cái đầu tiên
    words = s.strip().title().split()

    # Ghép các từ lại với nhau, cách nhau bởi một khoảng trắng
    optimized_string = ' '.join(words)

    return optimized_string

# Test với chuỗi đầu vào
s = " TRần duY thAnH "
print("Input:", s)
print("Output:", optimize_string(s))

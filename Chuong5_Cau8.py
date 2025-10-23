import os

def get_file_name_with_extension(path):
    return os.path.basename(path)

def get_file_name_without_extension(path):
    return os.path.splitext(os.path.basename(path))[0]

# Test hàm với đường dẫn bài hát
path = r"d:\\music\muabui.mp3"

# Lấy tên file có đuôi mở rộng
print("Tên file (bao gồm đuôi mở rộng):", get_file_name_with_extension(path))

# Lấy tên file không có đuôi mở rộng
print("Tên file (không bao gồm đuôi mở rộng):", get_file_name_without_extension(path))

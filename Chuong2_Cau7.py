#Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím

Một số cách nhập dữ liệu từ bàn phím trong Python:

1.Dùng hàm input() để nhập chuỗi:
name = input("Nhập tên: ")
2.Nhập số nguyên:
age = int(input("Nhập tuổi: "))
3.Nhập số thực:
score = float(input("Nhập điểm: "))
4.Nhập nhiều giá trị trên một dòng, dùng split():
a, b = input("Nhập hai số cách nhau bởi dấu cách: ").split()
a = int(a)
b = int(b)

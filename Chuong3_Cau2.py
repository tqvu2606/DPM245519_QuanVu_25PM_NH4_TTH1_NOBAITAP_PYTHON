print("Chương Trình Đếm Số Ngày Trong Tháng")
month = int(input("Nhập vào 1 tháng:"))
if month in (1,3,5,7,8,10,12):
    print("Tháng ", month, " Có 31 Ngày")
elif month in (4,6,9,11):
    print("Tháng ", month," Có 30 Ngày")
elif month == 2:
    year = int(input("Mời Bạn Nhập Vào Năm: "))
    if(year%4==0 and year % 100 != 0) or year % 400 == 0:
        print("Tháng ", month, " Có 29 Ngày")
    else:
        print("Tháng ", month, " Có 28 Ngày")
else:
    print("Tháng ", month, " Không Hợp Lệ")

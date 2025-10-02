print("Chương Trình Kiểm Tra Năm Nhuần")

year = int(input("Nhập Vào 1 Năm:"))

if(year%4==0 and year%100!=0) or year % 400 == 0:

    print("Năm ", year," là năm nhuần")

else:

    print("Năm ", year," là năm không nhuần")

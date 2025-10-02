#Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
Các loại lỗi khi lập trình Python gồm:

1.Lỗi cú pháp (SyntaxError): Viết sai quy tắc ngôn ngữ.
2.Lỗi logic: Chương trình chạy nhưng kết quả sai.
3.Lỗi runtime (ngoại lệ): Xảy ra khi chương trình đang chạy, ví dụ chia cho 0, truy cập phần tử không tồn tại.
Cách bắt lỗi trong Python là dùng khối try...except:
try:
    # code có thể gây lỗi
    x = int(input("Nhập số: "))
    y = 10 / x
except ValueError:
    print("Lỗi: Nhập không phải số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Chia cho 0!")
except Exception as e:
    print("Lỗi khác:", e)
else:
    print("Không có lỗi xảy ra.")
finally:
    print("Kết thúc chương trình.")
Khối try...except giúp chương trình không bị dừng đột ngột khi gặp lỗi.

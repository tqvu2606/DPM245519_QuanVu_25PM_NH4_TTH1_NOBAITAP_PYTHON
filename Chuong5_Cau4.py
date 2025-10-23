"""

Một số hàm quan trọng trong xử lý chuỗi của Python:

1) len(): Hàm này trả về độ dài của một chuỗi, tức là số ký tự trong chuỗi.

2) str.upper() và str.lower(): Các phương thức này chuyển đổi tất cả các ký tự trong chuỗi thành ký tự in hoa hoặc in thường.

3) str.strip(): Phương thức này loại bỏ các khoảng trắng ở đầu và cuối chuỗi.

4) str.split(sep): Phương thức này tách chuỗi thành một danh sách các chuỗi con bằng cách sử dụng dấu phân cách sep (mặc định là khoảng trắng).

5) str.join(iterable): Phương thức này kết hợp các phần tử trong iterable (ví dụ: danh sách hoặc bộ) thành một chuỗi, với chuỗi gọi phương thức làm dấu phân cách giữa các phần tử.

6) str.find(substring) và str.index(substring): Cả hai phương thức này đều trả về chỉ số đầu tiên của chuỗi con substring trong chuỗi gốc. Sự khác biệt chính là find() trả về -1 nếu không tìm thấy chuỗi con, trong khi index() sẽ gây ra một ngoại lệ ValueError.

7) str.replace(old, new): Phương thức này thay thế tất cả các lần xuất hiện của chuỗi con old trong chuỗi gốc bằng chuỗi con new.

8) str.startswith(prefix) và str.endswith(suffix): Cả hai phương thức này trả về True nếu chuỗi bắt đầu hoặc kết thúc bằng chuỗi con tương ứng.

9) str.isdigit(), str.isalpha(), str.islower(), str.isupper(): Các phương thức này kiểm tra xem chuỗi có chứa toàn bộ các ký tự số, chữ cái, chữ thường hoặc chữ hoa không và trả về True hoặc False tương ứng.

10) str.capitalize(): Phương thức này chuyển đổi ký tự đầu tiên của chuỗi thành chữ hoa, và tất cả các ký tự còn lại thành chữ thường.

"""

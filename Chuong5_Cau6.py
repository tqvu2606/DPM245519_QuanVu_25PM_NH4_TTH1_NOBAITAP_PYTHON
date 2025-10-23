import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các chuỗi số nguyên âm trong chuỗi đầu vào
    negative_numbers = re.findall(r'-\d+', s)
    
    # Xuất ra các số nguyên âm
    for num in negative_numbers:
        print(num)

# Test hàm với chuỗi đầu vào
s = "abc-5xyz-12k9l--p"
NegativeNumberInStrings(s)

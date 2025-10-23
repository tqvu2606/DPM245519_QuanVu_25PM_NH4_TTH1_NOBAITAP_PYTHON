"""
TH1:
def main():
    global val
    val = 5
    print(sum1(5)) # Gọi sum1(5), sẽ trả về 15 (1 + 2 + 3 + 4 + 5)
    print(sum2()) # Gọi sum2(), sẽ trả về 5 (1 + 2 + 3 + 4 + 5)
    print(sum3()) # Gọi sum3(), sẽ trả về 5 (5 + 4 + 3 + 2 + 1)

main()

Kết quả: 
15
5
5
"""

"""
TH2:
def main():
    global val
    val = 5
    print(sum1(5)) # Gọi sum1(5), sẽ trả về 15 (1 + 2 + 3 + 4 + 5)
    print(sum3()) # Gọi sum3(), sẽ trả về 15 (5 + 4 + 3 + 2 + 1)
    print(sum2()) # Gọi sum2(), sẽ trả về 5 (1 + 2 + 3 + 4 + 5)

main()
Kết quả:
15
15
5

"""

"""
TH3:
def main():
    global val
    val = 5
    print(sum2())   # Gọi sum2(), sẽ trả về 5 (1 + 2 + 3 + 4 + 5)
    print(sum1(5))  # Gọi sum1(5), sẽ trả về 15 (1 + 2 + 3 + 4 + 5)
    print(sum3())   # Gọi sum3(), sẽ trả về 5 (5 + 4 + 3 + 2 + 1)

main()

Kết quả:
5
15
5


"""

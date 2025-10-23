def input_sorted_sequence():
    while True:
        sequence = input("Nhập vào dãy số theo thứ tự tăng (các số cách nhau bằng khoảng trắng): ").strip()
        numbers = sequence.split()
        if all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1)):
            return list(map(float, numbers))
        else:
            print("Dãy số bạn nhập không theo thứ tự tăng. Hãy nhập lại!")

sequence = input_sorted_sequence()
print("Dãy số sau khi nhập xong:", sequence)

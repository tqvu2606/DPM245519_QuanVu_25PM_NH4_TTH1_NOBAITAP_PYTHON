def sort_decreasing_order(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

def input_and_sort():
    while True:
        try:
            n = int(input("Nhập số lượng số thực bạn muốn nhập: "))
            if n <= 0:
                print("Số lượng số phải lớn hơn 0. Hãy nhập lại!")
                continue
            break
        except ValueError:
            print("Bạn cần phải nhập một số nguyên. Hãy nhập lại!")

    sequence = []
    for i in range(n):
        while True:
            try:
                num = float(input(f"Nhập số thực thứ {i + 1}: "))
                sequence.append(num)
                break
            except ValueError:
                print("Bạn cần phải nhập một số thực. Hãy nhập lại!")
    
    sorted_sequence = sort_decreasing_order(sequence)
    return sorted_sequence

sorted_sequence = input_and_sort()
print("Dãy số sau khi sắp xếp giảm dần:", sorted_sequence)

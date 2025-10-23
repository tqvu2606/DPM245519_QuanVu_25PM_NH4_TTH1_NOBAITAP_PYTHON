def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Nhập hàng thứ {i+1} của ma trận, cách nhau bởi dấu cách: ").split()))
        if len(row) != cols:
            print("Số lượng phần tử của hàng không khớp với số cột. Nhập lại hàng!")
            row = input_matrix_row(cols)
        matrix.append(row)
    return matrix

def add_matrices(matrix_A, matrix_B):
    result = []
    for i in range(len(matrix_A)):
        row = []
        for j in range(len(matrix_A[0])):
            row.append(matrix_A[i][j] + matrix_B[i][j])
        result.append(row)
    return result

def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result

# Nhập số hàng và cột của ma trận A
rows_A = int(input("Nhập số hàng của ma trận A: "))
cols_A = int(input("Nhập số cột của ma trận A: "))

# Nhập ma trận A
print("Nhập ma trận A:")
matrix_A = input_matrix(rows_A, cols_A)

# Nhập số hàng và cột của ma trận B
rows_B = int(input("Nhập số hàng của ma trận B: "))
cols_B = int(input("Nhập số cột của ma trận B: "))

# Nhập ma trận B
print("Nhập ma trận B:")
matrix_B = input_matrix(rows_B, cols_B)

# Kiểm tra nếu hai ma trận có cùng kích thước
if rows_A != rows_B or cols_A != cols_B:
    print("Hai ma trận không cùng kích thước, không thể cộng.")
else:
    # Cộng hai ma trận
    result_matrix = add_matrices(matrix_A, matrix_B)
    print("Tổng của hai ma trận là:")
    for row in result_matrix:
        print(row)

# Tính ma trận hoán vị cho ma trận A
transposed_A = transpose_matrix(matrix_A)
print("Ma trận hoán vị của ma trận A là:")
for row in transposed_A:
    print(row)

# Tính ma trận hoán vị cho ma trận B
transposed_B = transpose_matrix(matrix_B)
print("Ma trận hoán vị của ma trận B là:")
for row in transposed_B:
    print(row)

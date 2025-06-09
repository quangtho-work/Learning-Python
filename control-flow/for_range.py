a = ['Mary', 'had', 'a', 'little', 'lamb']
print(a)
#range(start, stop, step)
"""
range dùng để lặp qua một dãy số, 
nếu muốn lặp qua một dãy văn bản thì cần phải sử dụng vòng lặp for 
hoặc dùng hàm len() để lấy độ dài của dãy văn bản.
"""
for i in range(len(a)):
    print(i, a[i] , end=" ")
print() 
for i in range(5):
    print(i, a[i], end=" ")
print() 
for i in range(1, 5):
    print(i, a[i], end=" ")
print()     
for i in range(1, 5, 2):
    print(i, a[i], end=" ")
print()  
for i in range(5, 0, -1):
    print(i, a[i-1], end=" ")
print()
for i in reversed(range(5, 0, -1)): # reversed để đảo ngược thứ tự
    print(i, a[i-1], end=" ")

#vòng lặp lồng nhau
# in ra ma trận bậc 2
print("\nMatrix:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
for i in range(len(matrix)): # lặp qua từng hàng của ma trận
    for j in range(len(matrix[i])): # lặp qua từng cột của hàng i
        # in ra phần tử ở hàng i, cột j
        print(matrix[i][j], end=" ")
    print()  # In xuống dòng sau mỗi hàng của ma trận
# in ra kim tư tháp
print("\nPyramid:")
n = 5  # Số hàng của kim tự tháp
for i in range(n):
    # In khoảng trắng trước mỗi hàng
    print(' ' * (n - i - 1), end='')
    # In dấu sao
    print('*' * (2 * i + 1))
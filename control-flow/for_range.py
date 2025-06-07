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
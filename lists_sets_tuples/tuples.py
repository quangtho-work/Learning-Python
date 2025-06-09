def print_tuple_info(t):
    print(t)
    print("Type:", type(t))
    print("Length:", len(t))
    print("First element:", t[0])
    print("Last element:", t[-1])
    print("Sliced tuple (1:3):", t[1:3])
    print("Concatenated tuple with (6, 7):", t + (6, 7))
    print("Repeated tuple (2 times):", t * 2)
    print("Is 'apple' in tuple?", 'apple' in t)
    print("Index of 'apple':", t.index('apple'))
    print("Count of 1 in tuple:", t.count(1))

if __name__ == "__main__":
    # tuples = () không thể sắp xếp, không thay đổi, không nhân bản
    # tuple là một chuỗi các phần tử không thay đổi, có thể chứa các kiểu dữ liệu khác nhau
    # tuple có thể chứa các kiểu dữ liệu không thay đổi (immutable) như số, chuỗi, tuple
    # tuple không thể thêm, xóa, cập nhật phần tử
    # tuple có thể chứa các kiểu dữ liệu khác nhau, bao gồm cả tuple lồng nhau
    # nhanh 
    t = (1, 'apple', 3.14, (2, 3), [4, 5])  # tuple chứa các kiểu dữ liệu khác nhau
    print("Original tuple:")
    print_tuple_info(t)
    print("---------------------------------------")
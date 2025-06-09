def delete_element(myset, element):
    # xóa phần tử trong tập hợp
    myset.discard(element)  # sử dụng discard
def add_element(myset, element):
    # thêm phần tử vào tập hợp
    myset.add(element)
def get_element(myset, element):
    # kiểm tra xem phần tử có trong tập hợp không
    return element in myset
def print_set(myset):
    # in tập hợp
    for item in myset:
        print(item, end=' ')
    print()
def update_element(myset, old_element, new_element):
    # cập nhật phần tử trong tập hợp
    if old_element in myset and new_element not in myset:
        myset.discard(old_element)  # xóa phần tử cũ
        myset.add(new_element)  # thêm phần tử mới
    else:
        print(f"{old_element} not found in the set.")
def reverse_set(myset):
    # tập hợp không thể đảo ngược, nhưng có thể chuyển đổi sang danh sách để đảo ngược
    reversed_set = list(myset)[::-1]
    return reversed_set

if __name__ == "__main__":
    # set = {} không thể sắp xếp, không thay đổi, không nhân bản 
    # tập hợp (set) là một tập hợp không có thứ tự và không có phần tử trùng lặp
    # tập hợp có thể chứa các kiểu dữ liệu không thay đổi (immutable) như số, chuỗi, tuple
    # có thể thêm, xóa phần tử

    myset = {1,'kẹo', "bánh", 4, 5, 5}
    print("Original set:")
    print_set(myset)
    print("---------------------------------------")
    # thêm phần tử vào tập hợp
    add_element(myset, 'trái cây')
    print("After adding 'trái cây':")
    print_set(myset)
    print("---------------------------------------")
    # xóa phần tử khỏi tập hợp
    delete_element(myset, 4)
    print("After deleting 4:")
    print_set(myset)
    print("---------------------------------------")
    # kiểm tra phần tử có trong tập hợp không
    element = 'kẹo'
    if get_element(myset, element):
        print(f"Element '{element}' is in the set.")
    else:
        print(f"Element '{element}' is not in the set.")
    print("---------------------------------------")
    # cập nhật phần tử trong tập hợp
    update_element(myset, 'kẹo', 'bánh kẹo')
    print("After updating 'kẹo' to 'bánh kẹo':")
    print_set(myset)
    print("---------------------------------------")
   
    # đảo ngược tập hợp (chuyển đổi sang danh sách)
    reversed_set = reverse_set(myset)
    print("Reversed set:")
    print(reversed_set)
    print("---------------------------------------")


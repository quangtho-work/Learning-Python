
def delete_element(lst, index):
    #xóa dự vào index
    if 0 <= index < len(lst):
        del lst[index]
    else:
        print("Index out of range.")
def add_element(lst, element):
    #thêm vào cuối danh sách
    lst.append(element)
def insert_element(lst, index, element):
   #thêm vào vị trí index
    if 0 <= index <= len(lst):
        lst.insert(index, element)
    else:
        print("Index out of range.")
def get_element(lst, index):
    #lấy phần tử tại vị trí index
    if 0 <= index < len(lst):
        return lst[index]
    else:
        print("Index out of range.")
        return None
def update_element(lst, index, element):
    #cập nhật phần tử tại vị trí index
    if 0 <= index < len(lst):
        lst[index] = element
    else:
        print("Index out of range.")
def sort_list(lst):
    #sắp xếp danh sách
    lst.sort()
def reverse_list(lst):
    #đảo ngược danh sách
    lst.reverse()
def print_list(lst):
    #in danh sách
    for item in lst:
        print(item, end=' ')
    print()      
if __name__ == "__main__":
    #list = [] có thể sắp xếp, thay đổi, nhân bản 
    languages = ['Python', 'Java', 'C++', 'JavaScript']
    print("Original list:")
    print_list(languages)
    print("---------------------------------------")
    #thêm phần tử vào cuối danh sách
    add_element(languages, 'Ruby') 
    print("After adding 'Ruby':")
    print_list(languages)
    print("---------------------------------------")
    #thêm phần tử vào vị trí index
    insert_element(languages, 2, 'Go')
    print("After inserting 'Go' at index 2:")
    print_list(languages)
    print("---------------------------------------")
    #lấy phần tử tại vị trí index

    element = get_element(languages, 1)
    if element is not None:
        print(f"Element at index 1: {element}")
    print("---------------------------------------")
    #cập nhật phần tử tại vị trí index
    update_element(languages, 0, 'Swift')
    print("After updating element at index 0 to 'Swift':")
    print_list(languages)
    print("---------------------------------------")
    #xoa phần tử tại vị trí index
    delete_element(languages, 3)
    print("After deleting element at index 3:")
    print_list(languages)
    print("---------------------------------------")
    #sắp xếp danh sách
    sort_list(languages)
    print("After sorting the list:")
    print_list(languages)

    print("---------------------------------------")
    #đảo ngược danh sách
    reverse_list(languages)

    print("After reversing the list:")
    print_list(languages)
    print("---------------------------------------")
    #sao chép danh sách
    copied_languages = languages.copy()
    print("Copied list:")
    print_list(copied_languages)


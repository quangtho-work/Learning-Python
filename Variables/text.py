
def string_methods():
    text = "Hello, World!" 
    # viết hoa
    upper_text = text.upper()
    # viết thường
    lower_text = text.lower()  
    # viết hoa chữ cái đầu tiên
    capitalized_text = text.capitalize()
    # thay thế
    replaced_text = text.replace("World", "Python")   
    # tách chuỗi theo dấu phẩy và khoảng trắng
    # (ví dụ: "Hello, World!" -> ["Hello", "World!"])
    split_text = text.split(", ") 
    #trả về  từ điển với các cặp key (khóa) và value (giá trị).
    return {
        "original": text,
        "upper": upper_text,
        "lower": lower_text,
        "capitalized": capitalized_text,
        "replaced": replaced_text,
        "split": split_text
    }
def string_formatting():
    name = "Alice"
    age = 30
    formatted_string = f"My name is {name} and I am {age} years old."
    formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
    formatted_string3 = "My name is %s and I am %d years old." % (name, age)
    return {
        "f-string": formatted_string,
        "str.format": formatted_string2,
        "percent_format": formatted_string3
    }
def string_concatenation():
    str1 = "Hello"
    str2 = "World"
    # nối chuỗi bằng dấu cộng
    concatenated_string = str1 + " " + str2
    # nối chuỗi bằng join
    concatenated_string2 = " ".join([str1, str2])
    return {
        "using_plus": concatenated_string,
        "using_join": concatenated_string2
    }
def string_slicing():
    text = "Hello, World!"
    # lấy 5 ký tự đầu tiên
    first_five = text[:5]  
    # lấy từ ký tự thứ 7 đến hết chuỗi
    from_seven = text[7:]  
    # lấy 4 ký tự đầu tiên
    first_four = text[0:4]  
    # lấy ký tự ở vị trí chẵn (bắt đầu từ 0)    
    every_second_char = text[::2]  
    # đảo ngược chuỗi
    reversed_text = text[::-1]
    return {
        "first_five": first_five,
        "from_seven": from_seven,
        "first_four": first_four,
        "every_second_char": every_second_char,
        "reversed_text": reversed_text
    }
def string_search():
    text = "Hello, World!"
    # tìm vị trí của ký tự 'o' nếu có trả về số lượng, nếu không có thì trả về -1
    index_of_o = text.find('o')  
    # kiểm tra xem chuỗi có chứa 'World' không. nếu có thì trả về True, nếu không có thì trả về False
    contains_world = 'World' in text  
    # đếm số lần xuất hiện của 'l' nếu có trả về số lượng, nếu không có thì trả về 0
    count_l = text.count('l')  
    return {
        "index_of_o": index_of_o,
        "contains_world": contains_world,
        "count_l": count_l
    }
def main():
    print("String Methods:")
    methods = string_methods() 
    # In ra các thuộc tính của biến methods và giá trị của chúng
    for key, value in methods.items(): 
        print(f"{key}: {value}")

    print("\nString Formatting:")
    formatting = string_formatting()
    for key, value in formatting.items():
        print(f"{key}: {value}")

    print("\nString Concatenation:")
    concatenation = string_concatenation()
    for key, value in concatenation.items():
        print(f"{key}: {value}")

    print("\nString Slicing:")
    slicing = string_slicing()
    for key, value in slicing.items():
        print(f"{key}: {value}")

    print("\nString Search:")
    search = string_search()
    for key, value in search.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    main()
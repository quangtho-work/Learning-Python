"""
list comprehensions là một cách ngắn gọn để tạo ra một danh sách mới
 từ một danh sách hiện có bằng cách áp dụng một biểu thức cho mỗi phần tử trong danh sách đó.
"""
def square_numbers(numbers):
    """
    Hàm này nhận vào một danh sách các số và trả về một danh sách mới  chứa bình phương của các số đó.
    """
    return [number ** 2 for number in numbers] # bình phương sử dụng **2

if __name__ == "__main__":
    # Ví dụ sử dụng hàm square_numbers
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = square_numbers(numbers)
    print(f"Bình phương của các số {numbers} là {squared_numbers}.")
    print("---------------------------------------------------")
    # vừa áp dụng vừa khai báo biến
    squared_numbers = [number * number for number in [1, 2, 3, 4, 5] if number > 1]
    print(f"Bình phương là {squared_numbers}.")
    
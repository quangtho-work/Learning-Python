import math
def test_conversion():
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            number2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    number3 = int(number1 + number2)
    print(f"The sum of {number1} and {number2} after conversion is {number3}")
def format_specifiers():
    number = 1234567890.1234567
    print(f"Default: {number}")
    print(f"Fixed-point: {number:.2f}") #in số thập phân với 2 chữ số sau dấu phẩy
    print(f"Scientific: {number:.2e}")  #in số khoa học với 2 chữ số sau dấu phẩy
    print(f"Percentage: {number:.2%}") #in số phần trăm với 2 chữ số sau dấu phẩy
    print(f"Width 20: {number:20}") #in số với độ rộng 20 ký tự
    print(f"Left-aligned: {number:<20}") #in số canh trái trong độ rộng 20 ký tự
    print(f"Right-aligned: {number:>20}") #in số canh phải trong độ rộng 20 ký tự
    print(f"Centered: {number:^20}")     #in số canh giữa trong độ rộng 20 ký tự
    print(f"Zero-padded: {number:020.2f}")   #in số với độ rộng 20 ký tự, canh phải và điền số 0 vào trước, với 2 chữ số sau dấu phẩy
def arithmetic_math():
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("Absolute value:", abs(number1))  # Trả về giá trị tuyệt đối
    print("Ceiling value:", math.ceil(number1))  # Làm tròn lên
    print("Floor value:", math.floor(number1))  # Làm tròn xuống
    print("Square root:", math.sqrt(number1))  # Căn bậc hai
    print("Power (number^2):", math.pow(number1, 2))  # Lũy thừa

def main():
    test_conversion()
    format_specifiers()
    arithmetic_math()
if __name__ == "__main__": # kiem tra neu file duoc chay truc tiep  
    main()

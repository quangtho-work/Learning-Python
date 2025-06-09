# calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def compare(x, y):
    if x > y:
        return f"{x} is greater than {y}"
    elif x < y:
        return f"{x} is less than {y}"
    else:
        return f"{x} is equal to {y}"

def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Compare")
        print("6. Exit")

        try:
            choice = int(input("Enter choice (1/2/3/4/5/6): "))           
            match choice:
                case 1:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    print(f"Result: {add(num1, num2)}")
                case 2:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    print(f"Result: {subtract(num1, num2)}")
                case 3:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    print(f"Result: {multiply(num1, num2)}")
                case 4:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    print(f"Result: {divide(num1, num2)}")
                case 5:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    print(compare(num1, num2))
                case 6:
                    print("Exiting the calculator. Goodbye!")
                    break
 
        except ValueError:
            print("Vui lòng nhập một số hợp lệ (1/2/3/4/5/6)!")


"""
python không có do-while, thay vào đó sử dụng vòng lặp while với một 
điều kiện luôn đúng ban đầu, và kiểm soát thoát vòng lặp bằng cách 
sử dụng break hoặc điều kiện khác bên trong khối code.
"""
if __name__ == "__main__":
    calculator()
    
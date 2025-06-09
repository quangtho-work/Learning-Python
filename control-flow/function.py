
# Khai báo hàm full_name trả về tên đầy đủ
def full_name(firstname, lastname):
    return firstname + " " + lastname


#khai báo hàm introduce in ra tên và tuổi
def introduce(name, age):
    print("Hello my name is", name, "and I am", age, "years old")

#khai báo hàm add_numbers trả về tổng của hai số
def add_numbers(num1, num2):
    return num1 + num2
# Khai báo hàm đệ quy 
def recursion(n):
    if n <= 0:
        return 0
    else:
        return n + recursion(n - 1)

if __name__ == "__main__":
    firstname="Thọ"
    lastname="Nguyễn Quang"
    age=22
    myname = full_name(firstname, lastname)
    # Gọi hàm full_name và in ra kết quả
    print("Full name:", myname)
    print("---------------------------------------")
    # Gọi hàm introduce
    introduce(myname, age)
    number1 = 10
    number2 = 20
    result = add_numbers(number1, number2)
    # Gọi hàm add_numbers và in ra kết quả
    print("The sum of", number1, "and", number2, "is", result)
    print("---------------------------------------")
    # Gọi hàm đệ quy
    n = 5
    print("The sum of numbers from 1 to", n, "is", recursion(n))
    print("---------------------------------------")
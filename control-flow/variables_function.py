firstname="Thọ"
lastname="Nguyễn Quang"
age=22
def full_name(firstname, lastname):
    return firstname + " " + lastname

myname = full_name(firstname, lastname)
print("Hello my name is", myname, "and I am", age, "years old")

number1 = 10
number2 = 20
#khai báo hàm add_numbers
def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(number1, number2)

print("The sum of", number1, "and", number2, "is", result)
def check_grade(studentName):
    grades = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "C",
        "David": "D",
        "Eve": "E"
    }
    
    if studentName in grades:
        return f"{studentName} has a grade of {grades[studentName]}."
    else:
        return f"{studentName} is not in the grade list."
def guessLetter(char):
    letters ="abcdefghijklmnopqrstuvwxyz"
    
    if char in letters:
        return f"{char} is in the list."
    else:
        return f"{char} is not in the list."
   
if __name__ == "__main__":
#in và not in để kiểm tra sự tồn tại của một phần tử trong một chuỗi hoặc danh sách
    print(check_grade(input("Enter student name: "))) #nhập tên học sinh
    print(guessLetter(input("Enter a letter: "))) #nhập một chữ cái
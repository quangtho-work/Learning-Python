# Một cách khác để sử dụng tính đa hình ngoài kế thừa
# Đối tượng chỉ cần có những thuộc tính/phương thức cần thiết tối thiểu
# "Nếu nó trông giống con vịt và kêu như con vịt, thì nó phải là con vịt."

class fakeHuman:
    id = 1
    def __init__(self, name, age, gender, madeBy):
        self.id = fakeHuman.id + 1
        fakeHuman.id += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.madeBy = madeBy
    
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Made by: {self.madeBy}")

    def update(self):
        self.name = input("Nhập tên mới: ")
        while True:
            try:
                self.age = int(input("Nhập tuổi mới: "))
                if self.age < 0:
                    print("Tuổi không thể là số âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Tuổi phải là một số nguyên. Vui lòng nhập lại.")
        self.gender = input("Nhập giới tính mới: ")
        self.madeBy = input("Nhập người tạo ra: ")
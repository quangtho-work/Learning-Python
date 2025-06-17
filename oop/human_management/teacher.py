from human import human

class teacher(human):
    def __init__(self, name, age, gender, certification, experience):
        super().__init__(name, age, gender)
        self.certification = certification
        self.experience = experience
        self.salary = 0

    def display(self):
        super().display()
        print(f"Certification: {self.certification}, Experience: {self.experience}, Salary: {self.salary}")

    def update(self):
        super().update()
        self.certification = input("Nhập chứng chỉ mới: ")
        while True:
            try:
                self.experience = int(input("Nhập số năm kinh nghiệm mới: "))
                if self.experience < 0:
                    print("Số năm kinh nghiệm không thể là số âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Số năm kinh nghiệm phải là một số nguyên. Vui lòng nhập lại.")

    def calculate_salary(self):
        if self.experience >= 1 and self.experience < 3:
            self.salary = 1000
        elif self.experience < 5:
            self.salary = 1500
        elif self.experience < 10:
            self.salary = 2000
        else:
            self.salary = 3000
from human import human

class student(human):
    def __init__(self, name, age, gender, grade, major, gpa):
        super().__init__(name, age, gender)
        self.grade = grade
        self.major = major
        self.gpa = gpa

    def display(self):
        super().display()
        print(f"Grade: {self.grade}, Major: {self.major}, GPA: {self.gpa}")

    def update(self):
        super().update()
        self.grade = input("Nhập lớp mới: ")
        self.major = input("Nhập chuyên ngành mới: ")
        while True:
            try:
                self.gpa = float(input("Nhập điểm trung bình (GPA) mới: "))
                if self.gpa < 0 or self.gpa > 4.0:
                    print("GPA phải trong khoảng từ 0 đến 4.0. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("GPA phải là một số thực. Vui lòng nhập lại.")

    def calculate_scholarship(self):
        if self.gpa >= 3.5:
            return "Full Scholarship"
        elif self.gpa >= 3.0:
            return "Half Scholarship"
        else:
            return "No Scholarship"
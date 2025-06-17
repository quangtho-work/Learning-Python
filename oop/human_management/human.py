# @abstractmethod dùng để định nghĩa một phương thức của lớp trừu tượng, khi lớp con kế thừa thì bắt buộc phải triển khai nó
# @staticmethod Phương thức tĩnh
# __init__	Khởi tạo đối tượng	
# __str__	Dùng trong print(obj)	
# __len__	Dùng trong len(obj)	
# __eq__	So sánh == giữa 2 object	
# __lt__	So sánh <	
# __getitem__	Truy cập phần tử obj[key]
# __setitem__	Thay đổi phần tử obj[key] = value
# __del__	Xóa đối tượng khỏi bộ nhớ
# __call__	Call đối tượng như hàm
# __getitem__	Truy cập phần tử obj[key]
class human:
    id = 1
    def __init__(self, name, age, gender):
        self.id = human.id + 1
        human.id += 1
        self.name = name
        self.age = age
        self.gender = gender
    
    def __lt__(self, other ):
        return self.age < other.age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

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
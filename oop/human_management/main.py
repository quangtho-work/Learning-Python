from human import human
from student import student
from teacher import teacher
from fakeHuman import fakeHuman
humans = []
def menu():
    while True:
        print("1. Thêm người")
        print("2. Xóa theo tên ")
        print("3. Sửa theo id")
        print("4. Hiển thị ")
        print("5. Tìm kiếm ")
        print("6. Sắp xếp theo tuổi")
        print("7. Thoát ")
        choice = int(input("Vui lòng chọn chức năng: "))
        if choice == 1:
            add_human()
        elif choice == 2:
            del_human()
        elif choice == 3:
            edit_human()
        elif choice == 4:
            show_all()
        elif choice == 5:
            search_human()
        elif choice == 6:
            sort_human()
        elif choice == 7:
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng nhập lại.")
            continue

def add_human():

    while True:

        choice = input("Bạn muốn thêm ? (1: Sinh viên, 2: Giáo viên , 3: Người khác, 4. Người nhân tạo , 5: Thoát): ")
        if choice == '1':
            name = input("Nhập tên: ")
            age = int(input("Nhập tuổi: "))
            gender = input("Nhập giới tính: ")
            grade = input("Nhập lớp: ")
            major = input("Nhập chuyên ngành: ")
            while True:
                try:
                    gpa = float(input("Nhập điểm trung bình (GPA): "))
                    if gpa < 0 or gpa > 4.0:
                        print("GPA phải trong khoảng từ 0 đến 4.0. Vui lòng nhập lại.")
                        continue
                    break
                except ValueError:
                    print("GPA phải là một số thực. Vui lòng nhập lại.")
            new_student = student(name, age, gender, grade, major, gpa)
            new_student.calculate_scholarship()
            humans.append(new_student)
        elif choice == '2':
            name = input("Nhập tên: ")
            age = int(input("Nhập tuổi: "))
            gender = input("Nhập giới tính: ")
            certification = input("Nhập chứng chỉ: ")
            while True:
                try:
                    experience = int(input("Nhập số năm kinh nghiệm: "))
                    if experience < 0:
                        print("Số năm kinh nghiệm không thể là số âm. Vui lòng nhập lại.")
                        continue
                    break
                except ValueError:
                    print("Số năm kinh nghiệm phải là một số nguyên. Vui lòng nhập lại.")
            new_teacher = teacher(name, age, gender, certification, experience)
            new_teacher.calculate_salary()
            humans.append(new_teacher)
        elif choice == '3':
            name = input("Nhập tên: ")
            age = int(input("Nhập tuổi: "))
            gender = input("Nhập giới tính: ")
            new_human = human(name, age, gender)
            humans.append(new_human)
        elif choice == '4':
            name = input("Nhập tên: ")
            age = int(input("Nhập tuổi: "))
            gender = input("Nhập giới tính: ")
            madeBy = input("Nhập người tạo ra: ")
            new_human = fakeHuman(name, age, gender, madeBy)
            humans.append(new_human)
        elif choice == '5':
            break
        else:
            print("Lựa chọn không hợp lệ.")
            continue
def del_human():
    name = input("Nhập tên đối tượng bạn muốn xóa: ")
    for i, human in enumerate(humans):
        if human.name == name:
            del humans[i]
            print(f"Đối tượng '{name}' đã được xóa.")
            return
    print(f"Không tìm thấy đối tượng tên '{name}'.")

def edit_human():
    if not humans:
        print("Danh sách rỗng.")
        return

    print("Danh sách đối tượng:")
    for human in humans:
        print(f"ID: {human.id} - Tên: {human.name}")

    try:
        id_to_edit = int(input("Nhập ID đối tượng bạn muốn sửa: "))
    except ValueError:
        print("ID phải là số nguyên.")
        return

    for human in humans:
        if human.id == id_to_edit:
            print(f"Đang sửa thông tin cho: {human.name}")
            human.update()  # Gọi update phù hợp theo lớp: student, teacher, hoặc human
            print("Cập nhật thành công.")
            return

    print(f"Không tìm thấy đối tượng với ID = {id_to_edit}.")

        
def show_all():
    for idx, h in enumerate(humans):
        print(f"\nĐối tượng thứ {idx+1}:")
        h.display()

def search_human():
    name = input("Nhập tên đối tượng bạn muốn tìm: ")
    for human in humans:
        if human.name == name:
            human.display()

def sort_human():
    humans.sort(reverse=True)

if __name__ == '__main__':
    menu()
    show_all()
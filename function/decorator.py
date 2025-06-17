# decorator dùng khi muốn thêm tính năng cho hàm mà không cần thay đổi hàm ban đầu
# dùng @decorator_name để thêm tính năng cho hàm
# @decorator_name
# def func_name():
#    pass

def add_age(function): # hàm thêm tuổi
    def inner(*args, **kwargs): # phải khai báo thêm hàm inner bên trong add_age để không tự chạy hàm add_age
        return function(*args, **kwargs) + " 20 tuổi"
    return inner
def add_height(function):
    def inner(*args, **kwargs):
        return function(*args, **kwargs) + " 170cm"
    return inner

@add_age
@add_height
def only_name(name):
    return f"Tên: {name}"
if __name__ == "__main__":
    print(only_name("Nguyễn Văn A")) 
    # khi gọi only_name thì sẽ gọi hàm theo thứ tự hàm được khai báo trên tên hàm 
    # vì @add_height gần nó thì sẽ gọi hàm add_height trước hàm add_age
def print_args(*args):
    """
    Hàm này nhận một số lượng không xác định các đối số và in chúng ra.
    :param args: Các đối số cần in ra
    """
    for arg in args:
        print(arg)
def print_kwargs(**kwargs):
    """
    Hàm này nhận một số lượng không xác định các đối số từ khóa và in chúng ra.
    :param kwargs: Các đối số từ khóa cần in ra
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")
def print_args_and_kwargs(*args, **kwargs):
    """
    Hàm này kết hợp cả hai hàm trên, nhận cả đối số và đối số từ khóa.
    :param args: Các đối số cần in ra
    :param kwargs: Các đối số từ khóa cần in ra
    """
    print_args(*args)
    print_kwargs(**kwargs)    

if __name__ == "__main__":
    print_args("Nguyễn Quang Thọ", "Ninh bình", 22) #in ra danh sách
    print_kwargs(name="Nguyễn Quang Thọ", age=22, city="Ninh Bình") #in ra từ khóa
    print_args_and_kwargs("Nguyễn Quang Thọ", "Ninh bình", 22, gender="Nam", hight=167, weight=67) #in ra cả danh sách và từ khóa

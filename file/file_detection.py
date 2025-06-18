import os
if __name__ == "__main__":
    
    # Đường dẫn tuyệt đối từ file hiện tại đến file text/test.txt
    base_dir = os.path.dirname(__file__)  # thư mục chứa file_detection.py
    print(base_dir)
    # Đường dẫn tuyệt đối đến file test.txt
    file_path = os.path.join(base_dir, "text", "test.txt")
    if os.path.exists(file_path):
        print(f"có file {file_path} tồn tại")
        if os.path.isfile(file_path):
            print("đây là file")
        elif os.path.isdir(file_path):
            print("đây là thư mục")    
    else:
        print("file không tồn tại")
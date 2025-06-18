"""
Đa luồng được sử dụng để thực hiện nhiều tác vụ đồng thời, 
như thể bạn đang làm nhiều việc cùng lúc. Ví dụ, bạn có thể học, 
nghe nhạc và ăn cùng một lúc.
Nó rất hữu ích cho các tác vụ bị giới hạn bởi I/O (input/output - nhập/xuất), 
chẳng hạn như đọc tệp (files) hoặc lấy dữ liệu từ một API. 
Những tác vụ này có thể mất một khoảng thời gian không xác định để hoàn thành
"""
import threading
import time
def walk():
    time.sleep(7)
    print('Walking')
def listen():
    time.sleep(5)
    print('Listening')
def think():
    time.sleep(3)
    print('Thinking')

if __name__ == '__main__':
    #nếu không dùng thread thì sẽ chạy lần lượt, rất mất thời gian
    # walk()
    # listen()
    # think()

    # nếu dùng thread thì sẽ chạy cùng lúc, không mất thời gian
    # dùng join để đợi thread chạy xong mới chạy tiếp
    t1 = threading.Thread(target=walk)
    t2 = threading.Thread(target=listen)
    t3 = threading.Thread(target=think)
    t1.start()
    t2.start()
    t3.start()
    t1.join() # join để đợi thread chạy xong mới chạy tiếp
    t2.join()
    t3.join()
    print('Done') # nếu không có join thì sẽ chạy dòng này ngay
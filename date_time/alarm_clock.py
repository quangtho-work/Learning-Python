import datetime
import time

def alarm_clock(timeset_str):
    message = "Dậy đi ông cháu ơi!"

    # Chuyển chuỗi thành đ datetime.time
    target_time = datetime.datetime.strptime(timeset_str, "%H:%M:%S").time()

    while True:
        now = datetime.datetime.now()
        current_time = now.time()
        print(current_time.strftime("%H:%M:%S"))

        if current_time >= target_time:
            print(message)
            button = input("Bấm phím bất kỳ để tắt\nNgủ thêm 5 phút nữa thì bấm 5: ")
            if button == "5":
                # Tạo datetime mới và cộng thêm 5 phút
                new_time = datetime.datetime.combine(datetime.date.today(), target_time) + datetime.timedelta(minutes=5)
                target_time = new_time.time()
                print("Ngủ thêm 5 phút nữa... ")
            else:
                break

        time.sleep(1)

if __name__ == "__main__":
    timeSet = input("Nhập giờ báo thức (HH:MM:SS): ")
    alarm_clock(timeSet)

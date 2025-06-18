import datetime
if __name__ == "__main__":

    now = datetime.datetime.now()
    print(now)
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.microsecond)
    print("Ngày: " + now.strftime("%Y-%m-%d"))
    print("Giờ: " + now.strftime("%H:%M:%S"))
    date = datetime.datetime(2019, 1, 1)
    print(date)

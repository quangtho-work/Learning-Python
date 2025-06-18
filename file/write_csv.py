import os
import csv # mảng lưu chữ theo ô giống excel
if __name__ == '__main__':

    human =[["name",'age','height','sex','address'],
                 ["nam",22,167,"male","newYork"],
                 ["bob",25,189,"male","cali"]]
    
    file_path = "files/test2.csv"
    f = open( file_path,'w', newline='') # mở file
    writer = csv.writer(f) # tạo đối tượng ghi
    for row in human:
        writer.writerow(row) # ghi dữ liệu vào file
    f.close()
    with open(file_path,'r') as f: # mở file
        content = csv.reader(f) # tạo đối tượng đọc
        for row in content:
            print(row)
        f.close()
import os
import json
import csv # mảng lưu chữ theo ô giống excel
if __name__ == '__main__':

    file_path = "files/test.txt"
    f = open( file_path,'w') # ghi file text
    f.write('hello world\n') # ghi chuoi vao file
    f.close()
    f = open(file_path,'r')
    print(f.read())
    f.close()
import os
import json
if __name__ == '__main__':

    human_json={
        'name':'zhangsan',
        'age':18,
        'height':180,
        'sex':'male',
        'address':'beijing'
    }
    file_path = "files/test1.json"
    f = open( file_path,'w') # ghi file text
    json.dump(human_json, f, indent=4) # ghi json vao file cach dau dong 4 ky tu
    f.close()
    f = open(file_path,'r')
    content = json.load(f)
    print(content)
    f.close()
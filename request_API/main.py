import requests # thư viện này phải được install trước cú pháp:  pip install requests

base_url="https://jsonplaceholder.typicode.com"

def get_User(id):
    url=base_url+"/users/"+ id
    print(url)
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        print(data)
    else:
        print("Error: ",response.status_code) 
if __name__=="__main__":
    get_User("1")
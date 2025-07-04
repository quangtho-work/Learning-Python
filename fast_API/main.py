from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
app = FastAPI()

class Blog(BaseModel):
    id: UUID                                               # Mỗi blog có một ID kiểu UUID
    title: str = Field(min_length=1)                       # Tiêu đề blog là chuỗi, không được để trống
    quantity: int = Field(gt=1, lt=100)                    # Số lượng phải lớn hơn 1 và nhỏ hơn 100
    published: Optional[bool]                              # Có thể có hoặc không, xác định đã được xuất bản hay chưa

Blogs = []

@app.post('/PostBlog')
def PostBlog(request: Blog):
    Blogs.append(request)                                 
    return request                                         

@app.get('/')
def GetBlog():
    return Blogs                                           

@app.put('/PutBlog/{id}')
def PutBlog(id: UUID, request: Blog):
    for index, b in enumerate(Blogs):                      
        if b.id == id:                                     
            Blogs[index].title = request.title             
            Blogs[index].quantity = request.quantity       
            Blogs[index].published = request.published     
            return Blogs[index]                           
    raise HTTPException(                                   
        status_code=404,
        detail=f"id: {id} do not exist"
    )

@app.delete('/DeleteBlog')
def DeleteBlog(id: UUID):
    for index, b in enumerate(Blogs):                     
        if b.id == id:                                     
            del Blogs[index]                               
            return f"ID: {id} deleted"                     
    raise HTTPException(                                  
        status_code=404,
        detail=f"id: {id} do not exist"
    )
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

posts = []

class Post(BaseModel):
    title : str
    content: str

@app.get("/posts", response_model=List[Post])
def get_posts():
    return posts

@app.post("/posts", response_model=Post)
def create_post(post:Post):
    posts.append(post)
    return post

@app.get(".post/{post_id}", response_model=Post)
def get_post(post_id: int):
    if post_id < 0 or post_id >= len(posts):
        return {"error": "게시글을 찾을 수 없습니다."}
    return posts[post_id]

@app.put("/posts/{post_id}",response_model=Post)
def update_post(post_id: int, update_post:Post):
    if post_id < 0 or post_id >= len(posts):
        return{"error":"게시글을 찾을 수 없습니다."}
    posts[post_id] = update_post
    return update_post

@app.delete("/posts/{post_id}")
def delete_post(post_id:int):
    if post_id < 0 or post_id >= len(posts):
        return {"error":"게시글을 찾을 수 없습니다."}
    delete_post = posts.pop(post_id)
    return {"message":"게시글이 삭제되었습니다.","delete_post":delete_post}
    

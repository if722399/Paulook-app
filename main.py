from time import time
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Union,List

app = FastAPI()

class Posts(BaseModel):
    n_likes: int
    description: str
    user_id: int
    creation_date: Union[datetime,None]=None
    post_id: int
    title_post: str

class Users(BaseModel):
    user_name: str
    user_id: int
    user_age: int
    user_rol: str
    rol_id: int
    career: Union[str, None] = None
    semester: Union[str, None] = None
    friends_list: list[int]

posts_dict = {}
user_dict = {}



@app.put('/posts')
def create_post(post: Posts):
    post = post.dict()
    posts_dict[post['post_id']] = post

    return {'Description':f'Post creado correctamente {post["post_id"]}'}


@app.put('/users')
def create_post(user: Users):
    user = user.dict()
    user_dict[user['user_id']] = user

    return {'Description':f'User creado correctamente {user["user_id"]}, su rol dentro de la institución es: {user["user_rol"]}'}

@app.post('/users/{user_id}/{friend_id}')
def update_user(user_id:int,friend_id:int):
    user = user_dict[user_id]
    list_to_update = user['friend_id']
    user_dict[user]['friend_id'] = list_to_update 
    return {'Description': 'Se ha creado correctamente'}

@app.get('/user/{user_id}/friends')
def get_friend_list(user_id: int):
    friends = user_dict[user_id]['friend_list']
    return {'User_ID':f'{user_id} friend list: {friends}'}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
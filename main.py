from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


app = FastAPI()


@app.get('/')
async def home():
    return {'message': 'hello world'}


@app.get('/items/')
async def items_show():
    return {'items': 'All items'}


@app.post('/items/')
async def item_add(item: Item):
    return item


@app.get('/items/{item_id}')
async def items_show(item_id: int, search: Optional[str] = None):
    return {'items': f'{item_id} {search}'}


@app.get('/users/')
async def users_list():
    return {"user_id": f"current user id"}


@app.get('/users/{user_id}')
async def users_read(user_id: int):
    return {"user_id": f"{user_id}"}

# @app.
# get
# post
# put
# patch
# delete
# options
# head
# trace

from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
async def home():
    return {'message': 'hello world'}


@app.get('/items/{item_id}')
async def items_show(item_id: int, search: Optional[str] = None):
    return {'items': f'{item_id} {search}'}

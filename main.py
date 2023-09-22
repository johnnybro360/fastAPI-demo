# https://realpython.com/fastapi-python-web-apis/
# https://fastapi.tiangolo.com/tutorial/
# https://realpython.com/async-io-python/
# https://realpython.com/python-async-features/
# https://realpython.com/python-type-checking/


from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
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
    item_dict = item.model_dump()
    if item.tax:
        tax_amount = item.price * item.tax / 100
        price_with_tax = item.price + tax_amount
        item_dict.update({"price_with_tax": price_with_tax, "tax_amount": tax_amount })
    return item_dict


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

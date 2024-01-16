from typing import Union
from fastapi import FastAPI
from router.product import product_router
from config.database import engine, Base
app = FastAPI()
app.title = "Mi aplicación para controlar stock"

app.include_router(product_router)


Base.metadata.create_all(bind=engine)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
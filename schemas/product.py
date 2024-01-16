from pydantic import BaseModel

class Product(BaseModel):
    name: str
    quantity: int
    price: float

    class Config:
        json_schema_extra = {
            "example" : {
                "id": 1,
                "name": "Mi producto",
                "quantity": 1,
                "price": 1.5
            }
        }
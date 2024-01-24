from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from services.product import ProductService
from schemas.product import Product
from fastapi.encoders import jsonable_encoder

product_router = APIRouter()

@product_router.get("/product/", tags=["Product"])
def get_products():
    db = Session()
    products = ProductService(db).get_products()
    if not products:
        return JSONResponse(status_code=404, content={"message": "No se encontraron productos"})
    return JSONResponse(status_code=200, content=jsonable_encoder(products))



@product_router.post("/product/", tags=["Product"])
def post_product(product:Product):
    db= Session()
    ProductService(db).create_product(product)
    return JSONResponse(status_code=200, content={"message": "Se ha registrado exitosamente"})
    
@product_router.delete("/product/{name}", tags=["Product"])
def delete_product(name):
    db= Session()
    ProductService(db).delete_product(name)
    return JSONResponse(status_code=200, content={"message": "Se ha elimnado exitosamente"})



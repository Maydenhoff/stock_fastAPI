from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Session
from models.product import Product

product_router = APIRouter()

@product_router.get("/", tags=["product"])
def get_products():
    db = Session()
    products = db.query(Product).all()
    if not products:
        return JSONResponse(status_code=404, content={"message": "No se encontraron productos"})
    return JSONResponse(status_code=200, content={"res": products})



@product_router.post("/", tags=["product"])
def post_product():
    db= Session()
    # db.add(product)
    return JSONResponse(status_code=200, content={"si": "funciona"})
    


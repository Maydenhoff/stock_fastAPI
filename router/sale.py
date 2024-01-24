from fastapi import APIRouter
from config.database import Session

sale_router = APIRouter()

@sale_router.get("/sale", tags=["Sale"])
def get_sales():
    db = Session()
    
    return "sola"
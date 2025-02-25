from fastapi import APIRouter, HTTPException
from app.models import Product
from app.database import collection

router = APIRouter()

@router.post("/")
def create_product(product: Product):
    result = collection.insert_one(product.dict())
    return {"id": str(result.inserted_id), "message": "Product created"}

@router.get("/")
def get_products():
    return list(collection.find({}, {"_id": 0}))

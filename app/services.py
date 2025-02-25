from app.database import collection

def find_product_by_id(product_id: str):
    return collection.find_one({"_id": product_id})

from fastapi import FastAPI
from app.routes import products

app = FastAPI()

# Inclure les routes
app.include_router(products.router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}

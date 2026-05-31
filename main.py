from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
    Product(id=2, name="phone", description="budget phone", price=99, quantity=22),
    Product(id=3, name="Pen", description="budget pen", price=9, quantity=2)
]

@app.get("/products")
def get_all_products():
    return products
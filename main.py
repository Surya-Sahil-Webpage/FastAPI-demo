from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Telusko Trac"

products = [
    Product(id=1, name="Phone", description="budget phone", price=99, quantity=1),
    Product(id=2, name="Pen", description="budget pen", price=9, quantity=2),
    Product(id=3, name="Table", description="small table", price=89, quantity=2),
    Product(id=4, name="Fan", description="budget fan", price=19, quantity=4)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product added successfully"
    return "product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)
            return "product deleted successfully"
    return "product not found"


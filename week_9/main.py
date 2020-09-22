from typing import Optional
from calculator import TaxCalculator
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/tax/{income}")
def calculate_tax(income: int):
    tc = TaxCalculator(income)
    tax = tc.calculate_tax()
    return {"tax": tax}
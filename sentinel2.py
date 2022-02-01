#!/usr/bin/env python3

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    #return "Oi"
    return {"str": "Hello, world!", "num": 1}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
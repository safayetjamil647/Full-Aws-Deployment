from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/category/{category_id}")
def read_item(category_id: int, q: Optional[str] = None):
    return {"category_id": category_id, "q": q}

from typing import Optional
import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/time")
def get_time(utc: Optional[bool] = False, format: Optional[str] = None):
    if utc:
        utcnow = datetime.datetime.utcnow()
        if format:
            return {"utc time formatted": utcnow.strftime(format)}
        else:
            return {"utc time unformatted": utcnow}
    else:
        now = datetime.datetime.now()
        if format:
            return {"nz time formatted": now.strftime(format)}
        else:
            return {"nz time unformatted": now}

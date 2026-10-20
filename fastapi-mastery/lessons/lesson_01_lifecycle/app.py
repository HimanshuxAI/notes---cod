"""Lesson 1 — a tiny app whose only job is to expose the machinery.

Run from the project root:

    uv run uvicorn lessons.lesson_01_lifecycle.app:app --reload
"""

import time

from fastapi import FastAPI, Request
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Mastery — Lesson 1",
    description="A tiny app whose only job is to expose the machinery.",
    version="0.1.0",
)


class Item(BaseModel):
    """The request body contract. Pydantic validates it before the endpoint runs."""

    name: str = Field(min_length=1, max_length=80)
    price: float = Field(gt=0)


@app.get("/health")
async def health() -> dict[str, str]:
    """The simplest possible route: no params, no body, deterministic output."""
    return {"status": "ok"}


@app.post("/items/{item_id}")
async def create_item(
    item_id: int,
    item: Item,
    request: Request,
) -> dict[str, object]:
    """FastAPI has already converted `item_id` to int and validated `item`
    by the time this function body starts executing."""
    return {
        "item_id": item_id,
        "item": item,
        "method": request.method,
        "path": request.url.path,
        "client": request.client.host if request.client else None,
    }


@app.get("/items/{item_id}")
async def read_item(
    item_id: int,
    q: str | None = None,
) -> dict[str, object]:
    """GET version. `q` is a query param because it is not in the path."""
    return {
        "item_id": item_id,
        "q": q,
        "name": "Keyboard",
        "price": 99.5,
    }


@app.get("/blocking")
def blocking() -> dict[str, str]:
    """A sync endpoint. FastAPI runs this in a worker thread so the event loop
    stays free. That is convenient — and a trap if you overuse it."""
    time.sleep(0.1)
    return {"mode": "sync endpoint -> threadpool"}  

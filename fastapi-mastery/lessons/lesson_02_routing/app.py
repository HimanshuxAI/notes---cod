"""Lesson 2 — routing and every input source.

Run from the project root:

    uv run uvicorn lessons.lesson_02_routing.app:app --reload
"""

from typing import Annotated

from fastapi import Cookie, FastAPI, Header, Path, Query, Response, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Mastery — Lesson 2",
    description="Path, query, header, cookie, body — and output control.",
    version="0.1.0",
)


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    email: str
    password: str = Field(min_length=8)


class UserRead(BaseModel):
    id: int
    username: str
    email: str


class Item(BaseModel):
    name: str
    price: float = Field(gt=0)


class Order(BaseModel):
    quantity: int = Field(ge=1)


# --- Path parameters and route ordering -------------------------------


@app.get("/users/me")
async def read_current_user() -> dict[str, str]:
    """Static route MUST be declared before /users/{user_id}."""
    return {"user": "current"}


@app.get("/users/{user_id}")
async def read_user(
    user_id: Annotated[int, Path(ge=1, le=1000, description="Numeric user id")],
) -> dict[str, int]:
    return {"user_id": user_id}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str) -> dict[str, str]:
    """`:path` lets the parameter swallow slashes."""
    return {"file_path": file_path}


# --- Query parameters -------------------------------------------------


@app.get("/search")
async def search(
    q: Annotated[str, Query(min_length=2, max_length=50, description="Search phrase")],
    tags: Annotated[list[str] | None, Query()] = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
) -> dict[str, object]:
    return {"q": q, "tags": tags, "limit": limit}


# --- Header and cookie parameters -------------------------------------


@app.get("/whoami")
async def whoami(
    user_agent: Annotated[str | None, Header()] = None,
    session_id: Annotated[str | None, Cookie()] = None,
) -> dict[str, str | None]:
    return {"user_agent": user_agent, "session_id": session_id}


# --- Body, path, query together, output control -----------------------


@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRead,
)
async def create_user(
    user: UserCreate,
    send_welcome: Annotated[bool, Query()] = False,
) -> dict[str, object]:
    # Pretend we saved to a DB and got an id back. `password` and
    # `send_welcome` are deliberately included to prove response filtering.
    return {
        "id": 1,
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "send_welcome": send_welcome,
    }


@app.post("/orders")
async def create_order(item: Item, order: Order) -> dict[str, object]:
    """Multiple Pydantic models -> one JSON body with two keys."""
    return {"item": item, "order": order}


# --- Setting response headers and cookies -----------------------------


@app.post("/login")
async def login(response: Response) -> dict[str, str]:
    response.headers["X-Demo"] = "lesson-2"
    response.set_cookie("session_id", "abc123", httponly=True, samesite="lax")
    return {"status": "logged-in"}

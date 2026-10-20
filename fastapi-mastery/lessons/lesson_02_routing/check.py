"""Run: uv run python -m lessons.lesson_02_routing.check

Verifies every input source and the route-ordering trap.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from lessons.lesson_02_routing.app import app

client = TestClient(app)


def show(label: str, response) -> None:
    print(f"\n{label}")
    print(f"  status: {response.status_code}")
    print(f"  body:   {response.json()}")
    if "x-demo" in response.headers:
        print(f"  x-demo: {response.headers['x-demo']}")
    if "set-cookie" in response.headers:
        print(f"  set-cookie: {response.headers['set-cookie']}")


# A deliberately broken app to prove that declaration order matters.
wrong_order = FastAPI()


@wrong_order.get("/users/{user_id}")
async def wrong_read_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}


@wrong_order.get("/users/me")
async def wrong_read_me() -> dict[str, str]:
    return {"user": "current"}


wrong_client = TestClient(wrong_order)


def main() -> None:
    show("GET /users/me (static first)", client.get("/users/me"))
    show("GET /users/42", client.get("/users/42"))
    show("GET /users/0 (Path(ge=1))", client.get("/users/0"))
    show("GET /users/abc (int parsing)", client.get("/users/abc"))
    show("GET /files/reports/2026/q1.pdf (:path)", client.get("/files/reports/2026/q1.pdf"))

    show(
        "GET /search?q=fastapi&tags=python&tags=web&limit=5",
        client.get(
            "/search",
            params=[("q", "fastapi"), ("tags", "python"), ("tags", "web"), ("limit", "5")],
        ),
    )
    show("GET /search (required q missing)", client.get("/search"))
    show("GET /search?q=f (too short)", client.get("/search", params={"q": "f"}))

    show("GET /whoami (no cookie)", client.get("/whoami"))
    client.cookies.set("session_id", "abc123")
    show("GET /whoami (with cookie)", client.get("/whoami"))
    client.cookies.clear()

    show(
        "POST /users (201 + response filtering)",
        client.post(
            "/users",
            json={
                "username": "alice",
                "email": "alice@example.com",
                "password": "secret123",
            },
        ),
    )
    show(
        "POST /users (password too short)",
        client.post(
            "/users",
            json={"username": "alice", "email": "alice@example.com", "password": "short"},
        ),
    )

    show(
        "POST /orders (multiple body models)",
        client.post(
            "/orders",
            json={"item": {"name": "Keyboard", "price": 99.5}, "order": {"quantity": 2}},
        ),
    )

    show("POST /login (response header + cookie)", client.post("/login"))

    show(
        "WRONG order: /users/{user_id} declared first",
        wrong_client.get("/users/me"),
    )


if __name__ == "__main__":
    main()

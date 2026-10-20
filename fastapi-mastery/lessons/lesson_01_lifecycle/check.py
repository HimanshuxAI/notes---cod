"""Run: uv run python -m lessons.lesson_01_lifecycle.check

Exercises 1-4 from Lesson 1, verified in-process (no server needed).
"""

import json

from fastapi.testclient import TestClient

from lessons.lesson_01_lifecycle.app import app

client = TestClient(app)


def show(label: str, response) -> None:
    print(f"\n{label}")
    print(f"  status: {response.status_code}")
    print(f"  body:   {response.json()}")


def main() -> None:
    # Exercise 1 + 2: read endpoint and optional query parameter.
    show("GET /items/42?q=keyboard", client.get("/items/42", params={"q": "keyboard"}))
    show("GET /items/42 (no q)", client.get("/items/42"))

    # Existing POST behaviour.
    show(
        "POST /items/42 (valid)",
        client.post("/items/42", json={"name": "Keyboard", "price": 99.5}),
    )

    # Exercise 3: validation failures.
    show(
        "POST /items/42 (price is a string)",
        client.post("/items/42", json={"name": "x", "price": "free"}),
    )
    show(
        "POST /items/42 (missing price)",
        client.post("/items/42", json={"name": "x"}),
    )
    show(
        "POST /items/42 (empty name + negative price)",
        client.post("/items/42", json={"name": "", "price": -3}),
    )

    # Exercise 4: the Item schema that powers /openapi.json and /docs.
    item_schema = app.openapi()["components"]["schemas"]["Item"]
    print("\nItem JSON Schema (from /openapi.json)")
    print(json.dumps(item_schema, indent=2))

    # The blocking endpoint still works.
    show("GET /blocking (sync endpoint)", client.get("/blocking"))


if __name__ == "__main__":
    main()

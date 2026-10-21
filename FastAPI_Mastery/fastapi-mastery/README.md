# FastAPI Mastery

A concept-first course. Each lesson is a runnable lab plus a mastery check.
The goal is not to memorize decorators — it is to be able to explain and debug
what happens between a TCP packet and a JSON response.

## Setup

```bash
cd fastapi-mastery
uv sync
uv run uvicorn lessons.lesson_01_lifecycle.app:app --reload
```

Then open <http://127.0.0.1:8000/docs>.

## Course map

| # | Lesson | Core question |
|---|--------|---------------|
| 01 | Lifecycle & architecture | What actually happens when a request arrives? |
| 02 | Routing & parameters | How does FastAPI turn HTTP into Python arguments? |
| 03 | Pydantic v2 | How do validation and serialization really work? |
| 04 | Dependency injection | Why is `Depends` the framework's superpower? |
| 05 | Async & concurrency | When does `async def` help, and when does it hurt? |
| 06 | Errors & middleware | How do I control every failure and every response? |
| 07 | Databases | Sessions, transactions, and the async SQLAlchemy stack. |
| 08 | Auth & security | OAuth2, JWT, password hashing, scopes. |
| 09 | Testing | Fast, isolated tests with dependency overrides. |
| 10 | Architecture | Routers, services, settings, lifespan, project layout. |
| 11 | Production | Workers, caching, observability, performance. |
| 12 | Advanced | WebSockets, SSE, streaming, uploads, OpenAPI internals. |

## How a lesson works

1. Read the concept note and the annotated code.
2. Run the lab and break it on purpose.
3. Do the exercises.
4. Answer the mastery check out loud, without looking.
5. Only then move on.

## Lesson 1

```bash
# Terminal 1
uv run uvicorn lessons.lesson_01_lifecycle.app:app --reload

# Terminal 2
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/items/42 \
  -H 'content-type: application/json' \
  -d '{"name": "Keyboard", "price": 99.5}'
```

Or run the self-checking script:

```bash
uv run python -m lessons.lesson_01_lifecycle.check
```

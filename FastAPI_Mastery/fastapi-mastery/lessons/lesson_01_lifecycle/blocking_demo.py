"""Lesson 1 stretch: why blocking inside `async def` is dangerous.

Run: uv run python -m lessons.lesson_01_lifecycle.blocking_demo

Two identical apps, two concurrent requests each:

- `def` endpoint  -> Starlette runs it in the threadpool, so both sleep together.
- `async def` + time.sleep -> blocks the event loop, so they serialize.
"""

import asyncio
import time

import httpx
from fastapi import FastAPI

DELAY = 0.2

sync_app = FastAPI()
async_app = FastAPI()


@sync_app.get("/work")
def sync_work() -> dict[str, str]:
    time.sleep(DELAY)
    return {"lane": "threadpool"}


@async_app.get("/work")
async def async_work() -> dict[str, str]:
    time.sleep(DELAY)  # BAD on purpose: blocks the event loop
    return {"lane": "event-loop-blocked"}


async def measure(app: FastAPI, label: str) -> None:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://demo") as client:
        started = time.perf_counter()
        await asyncio.gather(client.get("/work"), client.get("/work"))
        elapsed = time.perf_counter() - started
    print(f"{label}: {elapsed:.2f}s for 2 concurrent requests")


async def main() -> None:
    await measure(sync_app, "def + time.sleep        (threadpool)")
    await measure(async_app, "async def + time.sleep  (blocked loop)")


if __name__ == "__main__":
    asyncio.run(main())

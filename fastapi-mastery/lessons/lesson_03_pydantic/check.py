"""Run: uv run python -m lessons.lesson_03_pydantic.check"""

import uuid

from pydantic import ValidationError

from lessons.lesson_03_pydantic.schemas import (
    MemberAdd,
    OrgCreate,
    RegisterIn,
    Role,
    TokenOut,
    UserOut,
)
from lessons.lesson_03_pydantic.settings import Settings


def show_validation_error(label: str, exc: ValidationError) -> None:
    first = exc.errors()[0]
    print(f"{label}: 422 {first['type']} at {first['loc']}")


def main() -> None:
    print("=== Org name: strip BEFORE length validation ===")
    for name in ["  ", "  x  ", "  Acme  "]:
        try:
            print(f"{name!r} -> accepted as {OrgCreate(name=name).name!r}")
        except ValidationError as exc:
            show_validation_error(repr(name), exc)

    print("\n=== Email normalization ===")
    register = RegisterIn(
        email="  Alice@Example.COM  ",
        password="longenough",
        full_name="  Alice  ",
    )
    print("email:", register.email)
    print("full_name:", repr(register.full_name))

    print("\n=== Literal token type ===")
    print(TokenOut(access_token="abc").model_dump())
    try:
        TokenOut(access_token="abc", token_type="mac")
    except ValidationError as exc:
        show_validation_error("token_type='mac'", exc)

    print("\n=== Response model filtering (ORM-like object) ===")

    class FakeUser:
        id = uuid.UUID("00000000-0000-0000-0000-000000000001")
        email = "alice@example.com"
        full_name = "Alice"
        password_hash = "argon2id-secret"

    user_out = UserOut.model_validate(FakeUser())
    print("serialized:", user_out.model_dump())
    print("no password field:", "password_hash" not in user_out.model_dump())
    print("exclude email:", user_out.model_dump(exclude={"email"}))

    print("\n=== Enum round-trip ===")
    member = MemberAdd(email="bob@example.com")
    print("model:", member.model_dump())
    print("json:", member.model_dump_json())
    print("role is enum:", member.role is Role.viewer)

    print("\n=== JSON Schema is the API contract ===")
    name_schema = OrgCreate.model_json_schema()["properties"]["name"]
    print("OrgCreate.name:", name_schema)

    print("\n=== Settings ===")
    settings = Settings(
        database_url="postgresql+asyncpg://apib:apib@localhost:5432/apib",
        jwt_secret="x" * 32,
        jwt_expire_minutes="30",  # type: ignore[arg-type]  # env vars arrive as strings
        _env_file=None,
    )
    print("jwt_expire_minutes:", settings.jwt_expire_minutes, type(settings.jwt_expire_minutes).__name__)
    print("database_url scheme:", settings.database_url.split("://")[0])

    try:
        Settings(database_url="postgresql+asyncpg://localhost/db", jwt_secret="short", _env_file=None)
    except ValidationError as exc:
        show_validation_error("short jwt_secret", exc)

    try:
        Settings(_env_file=None)  # type: ignore[call-arg]
    except ValidationError as exc:
        print("missing required:", [error["loc"] for error in exc.errors()])


if __name__ == "__main__":
    main()

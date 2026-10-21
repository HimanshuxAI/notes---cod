"""Lesson 3 — Pydantic v2 schemas, modeled on Spigot's app/schemas.py.

This is the corrected/expanded version. Compare it with your repo.
"""

import uuid
from enum import Enum
from typing import Annotated, Literal

from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    StringConstraints,
)


class Role(str, Enum):
    admin = "admin"
    developer = "developer"
    viewer = "viewer"


# Strip first, THEN check length. "  " becomes "" and fails min_length.
OrgName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=2, max_length=120),
]

# Validate as an email, then normalize. EmailStr already lowercases the domain
# and strips surrounding whitespace; this also lowercases the local part.
NormalizedEmail = Annotated[
    EmailStr,
    AfterValidator(lambda value: value.strip().lower()),
]


# ---------- Auth ----------
class RegisterIn(BaseModel):
    email: NormalizedEmail
    password: str = Field(min_length=8, max_length=128)
    full_name: Annotated[
        str, StringConstraints(strip_whitespace=True, max_length=120)
    ] = ""


class TokenOut(BaseModel):
    access_token: str
    token_type: Literal["bearer"] = "bearer"


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr
    full_name: str


# ---------- Organisations ----------
class OrgCreate(BaseModel):
    name: OrgName


class OrgUpdate(BaseModel):
    name: OrgName


class OrgOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    role: Role


class MemberAdd(BaseModel):
    email: NormalizedEmail
    role: Role = Role.viewer


class MemberRoleUpdate(BaseModel):
    role: Role


class MemberOut(BaseModel):
    user_id: uuid.UUID
    email: EmailStr
    full_name: str
    role: Role

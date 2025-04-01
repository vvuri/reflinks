import secrets
import time
import uuid
from typing import Annotated, Any
from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="/demo", tags=["Demo Auth"])

security = HTTPBasic()


@router.get("/basic-auth-test/")
def demo_basic_auth_test(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {
        "message": "Hi!",
        "username": credentials.username,
        "password": credentials.password,
    }


username_to_passwords = {
    "admin": "admin",
    "user": "123",
}

token_to_username = {
    "64f13d910dc52a9d40798bc3825d2a42": "admin",
    "2c5bc3e7c04a9a56ba5c69cba283a505": "123",
}


def get_auth_username_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> str:
    un_authed = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_password = username_to_passwords.get(credentials.username)
    if correct_password is None:
        raise un_authed

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        correct_password.encode("utf-8"),
    ):
        raise un_authed

    return credentials.username


def get_auth_username_header(static_token: str = Header(alias="x-auth-token")) -> str:
    if username := token_to_username.get(static_token):
        return username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
    )


@router.get("/basic-auth/")
def demo_basic_auth_credentials(
    auth_username: str = Depends(get_auth_username_credentials),
):
    return {
        "message": f"Hi {auth_username}!",
    }


@router.get("/basic-auth-header/")
def demo_basic_auth_header(username: str = Depends(get_auth_username_header)):
    return {
        "message": f"Hi {username}!",
    }


COOKIES: dict[str, dict[str, Any]] = {}
COOKIE_ID_KEY = "app-session-id"


def generate_session_id() -> str:
    return uuid.uuid4().hex


def get_session_data(
    session_id: str = Cookie(alias=COOKIE_ID_KEY),
) -> dict:
    if session_id not in COOKIES:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorised",
        )
    return COOKIES[session_id]


@router.post("/login-cookie/")
def auth_login_cookie(
    response: Response,
    # auth_username: str = Depends(get_auth_username_credentials)
    auth_username: str = Depends(get_auth_username_header),
):
    session_id = generate_session_id()
    response.set_cookie(COOKIE_ID_KEY, session_id)
    COOKIES[session_id] = {
        "username": auth_username,
        "login_at": int(time.time()),
    }
    return {"result": "ok"}


@router.get("/check-cookie")
def check_login_cookie(user_session_date: dict = Depends(get_session_data)):
    username = user_session_date["username"]
    return {
        "user": username,
        **user_session_date,
    }


@router.get("/logout-cookie")
def logout_login_cookie(
    response: Response,
    session_id: str = Cookie(alias=COOKIE_ID_KEY),
    user_session_date: dict = Depends(get_session_data),
):
    username = user_session_date["username"]
    COOKIES.pop(session_id)
    response.delete_cookie(COOKIE_ID_KEY)
    return {
        "user": username,
    }

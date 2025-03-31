from typing import List, Dict
from fastapi import APIRouter, HTTPException, status
import uuid
from loguru import logger

from ..models.links import UrlLink, ClientUrlLink

link_router = APIRouter(tags=["Ref Links"])

def get_new_id():
    return uuid.uuid4()


@link_router.get("/link/{link_id}")
def get_link(link_id: uuid) -> UrlLink:
    logger("get_link:", link_id)
    return {"id": "A-1", "urt":"u1"}


@link_router.get("/links")
def get_all_links() -> List[UrlLink]:
    logger.info("get_all_links")
    return [{"id": "A-1", "urt":"u1"},{"id": "A-2", "urt":"u2"},{"id": "A-3", "urt":"u3"},{"id": "A-4", "urt":"u4"}]


@link_router.post("/add")
def add_link(body: ClientUrlLink) -> Dict:
    logger.info("add_link:", body.url)
    return {"id": "A-10","status": "padding", "message":"link add in queue"}

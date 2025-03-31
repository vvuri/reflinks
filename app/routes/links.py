from typing import List, Dict
from fastapi import APIRouter, HTTPException, status
import uuid
from loguru import logger

from ..models.links import UrlLink, ClientUrlLink

link_router = APIRouter(tags=["Ref Links"])

def get_new_id():
    return uuid.uuid4()


@link_router.get("/image/{link_id}")
def get_image(link_id: uuid) -> Dict:
    logger.info("get_image:", link_id)
    return {"message":"image"}


@link_router.get("/link/{link_id}")
def get_link(link_id: uuid) -> Dict:
    logger.info("get_link:", link_id)
    return {"id": "A-1", "urt": "u1"}


@link_router.post("/link/add")
def add_link(body: ClientUrlLink) -> Dict:
    logger.info("add_link:", body.url)
    return {"id": "A-10","status": "padding", "message": "link add in queue"}


@link_router.put("/link/{id}")
def update_link(body: UrlLink) -> Dict:
    logger.info("update_link_data:", body.url)
    return {"id": "A-10", "message":"link update"}


@link_router.get("/links")
def get_all_links() -> List[Dict]:
    logger.info("get_all_links")
    return [{"id": "A-1", "urt":"u1"},{"id": "A-2", "urt":"u2"},{"id": "A-3", "urt":"u3"},{"id": "A-4", "urt":"u4"}]

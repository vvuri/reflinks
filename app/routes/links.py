from typing import List, Dict
from fastapi import APIRouter, HTTPException, status
import uuid

from models.links import UrlLink

link_router = APIRouter(tags=["Ref Links"])

def get_new_id():
    return uuid.uuid4()

@link_router.get("/")
def get_all_links() -> List[UrlLink]:
    return [{"id": "A-1", "urt":"u1"},{"id": "A-2", "urt":"u2"},{"id": "A-3", "urt":"u3"},{"id": "A-4", "urt":"u4"}]

@link_router.post("/add")
def add_link(body: UrlLink) -> Dict:
    return {"message": "add link","status": "success"}

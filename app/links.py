from fastapi import APIRoute

import uuid


router = APIRouter(prefix="/api/links/", tags=["Ref Links"])


def get_new_id():
    return uuid.uuid4()

@router.get("/add")
def read_root():

    return {"ADD"}


from pydantic import BaseModel, HttpUrl, UUID4


class UrlLink(BaseModel):
    url: HttpUrl
    id: UUID4

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://mylink.image/1.jpg",
                "id": "16fd2706-8baf-433b-82eb-8c7fada847da",
            }
        }

class ClientUrlLink(BaseModel):
    url: HttpUrl

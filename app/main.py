import uvicorn

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.links import link_router

app = FastAPI()

app.include_router(link_router,  prefix="/api/links")

@app.get('/api/version')
def version() -> dict:
    return {'ver': '0.0.1'}

@app.get('/')
def index():
    return RedirectResponse(url="/home/")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

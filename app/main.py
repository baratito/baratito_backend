from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from structlog import get_logger

app = FastAPI()


log = get_logger()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="/static"), name="static")


@app.get("/")
@app.get("/")
async def main():
    log.info("testing structlog", out_of_the_box=True, effort=0)
    return "Hi!"

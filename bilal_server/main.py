from fastapi import FastAPI
from bilal_server.models import media_info
from bilal_server.play_athan import execute_athan
from fastapi.middleware.cors import CORSMiddleware

# creating instance of FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# just Hello World for now
@app.get("/")
async def root():
    return "Hello World"


# play a sound with input as Goolge Drive file ID
@app.post("/sound")
# update this so it pulls defaults from config
async def sound(media_info: media_info):
    response = execute_athan(media_info.audio_id, media_info.speaker)
    return response

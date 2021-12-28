from pydantic import BaseModel

class media_info(BaseModel):
    speaker: str
    audio_id: str

    class Config:
        schema_extra = {
            "example": {
                "speaker" : "Studio Display",
                "audio_id" : "1UWIc6YVaGgRJGzbRk4yfN1vbcS5ud4eC",
            }
        }
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from engine.current import EthereaEngine
from io import BytesIO

router = APIRouter()

# -----------------------------
# Request models
# -----------------------------
class VoiceMessage(BaseModel):
    user_id: str
    input_type: str = "voice"    # always voice
    voice_output: bool = True    # default True

# -----------------------------
# In-memory engine instances
# -----------------------------
engines = {}

def get_engine(user_id: str) -> EthereaEngine:
    if user_id not in engines:
        engines[user_id] = EthereaEngine(user_id=user_id)
    return engines[user_id]

# -----------------------------
# Routes
# -----------------------------
@router.post("/api/voice")
async def process_voice(user: VoiceMessage, file: UploadFile = File(...)):
    """
    Accepts a voice file and returns AI response (text + optional audio).
    """
    engine = get_engine(user.user_id)
    try:
        # Read audio file bytes
        audio_bytes = await file.read()
        # Process voice input via engine
        response = await engine.process_input(
            user_input=BytesIO(audio_bytes), 
            input_type="voice", 
            voice_output=user.voice_output
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# MINDFULSCREEN/Etherea Living OS/api_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from engine.current import EthereaEngine
from hybrid_interface_memory import load_user_memory

router = APIRouter()

# -----------------------------
# Request Models
# -----------------------------
class UserID(BaseModel):
    user_id: str

class UserSettingsUpdate(BaseModel):
    user_id: str
    personality: str = None  # optional update

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
@router.get("/api/history")
def get_history(user: UserID):
    try:
        memory = load_user_memory(user.user_id)
        return {"user_id": user.user_id, "memory": memory}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/settings")
def update_settings(settings: UserSettingsUpdate):
    try:
        engine = get_engine(settings.user_id)
        if settings.personality:
            from personality_engine import PersonalityEngine
            engine_personality = PersonalityEngine()
            engine_personality.set_personality(settings.personality)
        return {"status": "success", "message": "Settings updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# MINDFULSCREEN/Etherea Living OS/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from ai_engine import inference, preprocessing, model_manager
from chat_system import chat_ai
from voice_system import tts, stt, commands
import asyncio

app = FastAPI(title="ETHEREA - Living OS API")

# Allow CORS for frontend React connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routes
# -----------------------------

@app.get("/")
async def root():
    return {"status": "ETHEREA API running"}

@app.post("/api/message")
async def handle_message(request: Request):
    """
    Receives user input (text or voice)
    Processes via AI engine and chat system
    Returns response
    """
    data = await request.json()
    user_input = data.get("message", "")
    input_type = data.get("type", "text")  # 'text' or 'voice'

    # If voice, convert to text
    if input_type == "voice":
        user_input = stt.transcribe_audio(user_input)

    # Preprocess input
    processed_input = preprocessing.clean_input(user_input)

    # Run AI inference
    ai_response = inference.generate_response(processed_input)

    # Chat system integration
    chat_reply = chat_ai.get_chat_response(ai_response, user_input)

    # Convert to speech if requested
    if data.get("voice_output", False):
        audio_file = tts.speak(chat_reply)
        return {"response": chat_reply, "audio_file": audio_file}

    return {"response": chat_reply}

@app.get("/api/history")
async def get_history(user_id: str):
    """
    Fetch user conversation history
    """
    history = chat_ai.get_user_history(user_id)
    return {"history": history}

@app.post("/api/settings")
async def update_settings(request: Request):
    """
    Update user personalization / personality settings
    """
    data = await request.json()
    user_id = data.get("user_id")
    settings = data.get("settings", {})
    chat_ai.update_user_settings(user_id, settings)
    return {"status": "Settings updated"}

# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
async def startup_event():
    print("ETHEREA API starting...")
    model_manager.load_models()  # load all AI models on startup
    print("Models loaded successfully.")

# -----------------------------
# Run with: uvicorn main:app --reload
# -----------------------------

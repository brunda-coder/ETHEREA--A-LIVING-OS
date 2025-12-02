# MINDFULSCREEN/Etherea Living OS/engine.current.py

import asyncio
from ai_engine import model_manager, inference, preprocessing
from chat_system import chat_ai
from voice_system import tts, stt, commands
from hybrid_interface_memory import load_user_memory, save_user_memory
from personality_engine import personalize_response

class EthereaEngine:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.memory = load_user_memory(user_id)
        model_manager.load_models()
        print(f"[EthereaEngine] Initialized for user: {self.user_id}")

    async def process_input(self, user_input: str, input_type: str = "text", voice_output: bool = False):
        # 1️⃣ Convert voice to text if needed
        if input_type == "voice":
            user_input = stt.transcribe_audio(user_input)
        
        # 2️⃣ Preprocess input
        cleaned_input = preprocessing.clean_input(user_input)

        # 3️⃣ AI engine response
        ai_reply = inference.generate_response(cleaned_input)

        # 4️⃣ Personalize
        personalized_reply = personalize_response(ai_reply, self.memory)

        # 5️⃣ Chat system integration
        chat_reply = chat_ai.get_chat_response(personalized_reply, user_input)

        # 6️⃣ Save memory
        self.memory.append({"user": user_input, "ai": chat_reply})
        save_user_memory(self.user_id, self.memory)

        # 7️⃣ Convert to voice if requested
        audio_file = None
        if voice_output:
            audio_file = tts.speak(chat_reply)

        return {"text": chat_reply, "audio_file": audio_file}

# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    engine = EthereaEngine(user_id="test_user")

    async def main():
        response = await engine.process_input("Hello Etherea! How are you?", input_type="text", voice_output=False)
        print("Response:", response["text"])

    asyncio.run(main())


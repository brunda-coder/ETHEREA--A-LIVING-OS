# commands.py
from tts import TTS
from stt import STT

class VoiceSystem:
    """
    Integrates TTS + STT and connects to AI engine.
    """

    def __init__(self, ai_engine=None):
        self.tts = TTS()
        self.stt = STT()
        self.ai_engine = ai_engine

    def interact(self):
        """Listen to user, get AI prediction, speak response."""
        user_input = self.stt.listen()
        print(f"User said: {user_input}")

        if self.ai_engine:
            response = self.ai_engine.predict(user_input)
            response_text = f"AI prediction: {response:.2f}"
        else:
            response_text = "No AI engine connected."

        print(f"Etherea says: {response_text}")
        self.tts.speak(response_text)

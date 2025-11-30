# tts.py
import pyttsx3

class TTS:
    """
    Text-to-Speech engine for Etherea.
    """

    def __init__(self, voice_rate=150, voice_id=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', voice_rate)
        voices = self.engine.getProperty('voices')
        if voice_id is not None:
            self.engine.setProperty('voice', voices[voice_id].id)
        else:
            self.engine.setProperty('voice', voices[0].id)

    def speak(self, text):
        """Convert text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

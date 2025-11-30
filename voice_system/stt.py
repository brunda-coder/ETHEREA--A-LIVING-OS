# stt.py
import speech_recognition as sr

class STT:
    """
    Speech-to-Text engine for Etherea.
    """

    def __init__(self, microphone_index=None):
        self.recognizer = sr.Recognizer()
        self.microphone_index = microphone_index

    def listen(self):
        """Listen and convert speech to text."""
        mic = sr.Microphone(device_index=self.microphone_index)
        with mic as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "[Unrecognized speech]"
        except sr.RequestError:
            return "[API unavailable]"

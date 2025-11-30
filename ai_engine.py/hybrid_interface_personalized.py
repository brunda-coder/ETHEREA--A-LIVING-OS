# hybrid_interface_personalized.py

from ai_engine.hybrid_interface import HybridAIInterface
from ai_engine.personality_engine.personality import PersonalityEngine


class PersonalizedHybridAI:
    """
    This layer wraps the hybrid interface and adds personality-controlled output.
    """

    def __init__(self, personality_style="balanced"):
        self.ai = HybridAIInterface()
        self.personality = PersonalityEngine(default_style=personality_style)

    def set_personality(self, style):
        """Switch AI personality at runtime."""
        self.personality.set_style(style)

    def ask(self, user_message):
        """
        Send user message to hybrid AI → get raw answer → apply personality.
        """
        raw_ai_text = self.ai.query(user_message)
        final_text = self.personality.format_response(raw_ai_text)
        return final_text

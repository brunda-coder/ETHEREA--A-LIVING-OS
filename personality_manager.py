# personality_manager.py

from personality_engine import PersonalityEngine

class PersonalityManager:
    """
    Connects AI engine responses to existing PersonalityEngine for styled outputs.
    """

    def __init__(self, ai_engine=None):
        self.ai_engine = ai_engine
        self.personality = PersonalityEngine(default_style="friendly")

    def set_personality(self, style_name):
        """
        Change the personality style dynamically
        """
        return self.personality.set_style(style_name)

    def get_personality(self):
        """
        Retrieve current personality style
        """
        return self.personality.get_style()

    def get_ai_response(self, user_input):
        """
        Get AI engine response formatted according to current personality
        """
        if self.ai_engine:
            raw_response = self.ai_engine.predict(user_input)
            # Format the response using the personality
            styled_response = self.personality.format_response(f"{raw_response:.2f}")
            return styled_response
        else:
            return self.personality.format_response("AI engine not connected.")

# personality_engine.py

class PersonalityEngine:
    """
    True system-level personality controller.
    Works like ChatGPT-5.x tone conditioning.
    It does NOT wrap or repeat output text.
    It only provides personality instructions
    to the AI model during generation.
    """

    def __init__(self, default="balanced"):
        self.current = default

        # System-level personality definitions
        self.styles = {
            "balanced": "Respond with a natural, helpful, human-like tone.",
            "friendly": "Respond warmly and enthusiastically. Be encouraging.",
            "creative": "Use imaginative, expressive language with flair.",
            "professional": "Respond with clarity, precision, and formality.",
            "playful": "Be witty, fun, mischievous, and lighthearted.",
            "empathetic": "Be gentle, soothing, emotionally understanding.",
            "minimalist": "Keep responses short, clean, and direct.",
            "brunda_signature": (
                "Speak with poetic clarity, boldness and elegance. "
                "Express warmth, confidence, and artistic phrasing."
            )
        }

    # -----------------------
    # Public API
    # -----------------------

    def set_personality(self, persona_name):
        """Switch the global personality."""
        if persona_name in self.styles:
            self.current = persona_name
        else:
            raise ValueError(f"Unknown personality: {persona_name}")

    def get_system_instruction(self):
        """
        Returns the tone instruction that the AI model
        should use before generating a response.
        (This is how ChatGPT modifies tone.)
        """
        return self.styles.get(self.current, self.styles["balanced"])

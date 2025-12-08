# chat_manager.py
"""
Chat manager: typed chat + memory + personality glue.
Relies on existing repo pieces:
 - hybrid_interface_memory.py  (provides AI query/predict capability)
 - personality_manager.py     (provides personality styling)
 - conversation_memory.py     (local storage for turns)
"""

import os
from pathlib import Path

# Try to import existing components in your repo
try:
    from hybrid_interface_memory import setup_ai_engine, Hybrid-like  # placeholder safe check
except Exception:
    # We'll use hybrid_interface.py (your repo has hybrid_interface.py). The file typically has a main interface.
    try:
        from hybrid_interface import setup_ai_engine  # function that returns engine / interface
    except Exception:
        setup_ai_engine = None

# Personality manager (should exist at repo root)
try:
    from personality_manager import PersonalityManager
except Exception:
    PersonalityManager = None

# Local memory helper
from conversation_memory import ConversationMemory

class ChatManager:
    """
    High-level chat manager:
     - accepts typed input
     - queries the AI engine
     - styles response with personality manager
     - stores turn in conversation memory
    """

    def __init__(self, ai_engine=None, persona="friendly"):
        # if ai_engine is None, try to set up using repo helper
        if ai_engine is None and callable(setup_ai_engine):
            try:
                self.ai = setup_ai_engine()
            except Exception:
                self.ai = None
        else:
            self.ai = ai_engine

        self.personality = PersonalityManager(ai_engine=self.ai) if PersonalityManager else None
        if self.personality:
            self.personality.set_personality(persona)
        self.memory = ConversationMemory()

    def _query_ai(self, text):
        """
        Query AI engine. Prefer higher-level method if available.
        Expectation: the AI engine has either .predict(text) or .query(text)
        """
        if not self.ai:
            return "AI engine not available."

        # try predict
        try:
            resp = self.ai.predict(text)
            # some models return numeric; cast to str
            if isinstance(resp, (int, float)):
                return str(resp)
            return resp
        except Exception:
            pass

        # try query
        try:
            resp = self.ai.query(text)
            return resp
        except Exception:
            pass

        return "AI engine could not generate a response."

    def send(self, user_text):
        # 1. Query AI
        raw = self._query_ai(user_text)

        # 2. Style via personality manager (if present)
        if self.personality:
            styled = self.personality.get_ai_response(user_text)  # personality_manager returns styled response
        else:
            styled = str(raw)

        # 3. Save to memory
        persona_name = self.personality.get_personality() if self.personality else ""
        self.memory.add_turn(user_text, styled, persona=persona_name)

        # 4. Return final text
        return styled

    def history(self, limit=20):
        return self.memory.load_memory(limit=limit)

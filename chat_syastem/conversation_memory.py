# conversation_memory.py
import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "..", "memory.json")

class ConversationMemory:
    """
    Simple, robust conversation memory helper.
    Stores a list of turns: {timestamp, user, ai, persona}
    """

    def __init__(self, memory_file=None):
        self.memory_file = memory_file or os.path.abspath(MEMORY_FILE)
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f, indent=2)

    def add_turn(self, user_text, ai_text, persona=None):
        memory = self.load_memory()
        memory.append({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "user": user_text,
            "ai": ai_text,
            "persona": persona or ""
        })
        with open(self.memory_file, "w") as f:
            json.dump(memory, f, indent=2)

    def load_memory(self, limit=None):
        with open(self.memory_file, "r") as f:
            memory = json.load(f)
        if limit:
            return memory[-limit:]
        return memory

    def clear(self):
        with open(self.memory_file, "w") as f:
            json.dump([], f, indent=2)

# memory_manager.py
import json
import os

class MemoryManager:
    """
    Handles storing and retrieving conversation memory for Etherea.
    """

    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        if not os.path.exists(memory_file):
            with open(memory_file, "w") as f:
                json.dump([], f)

    def add_memory(self, user_input, ai_response):
        """Save a single conversation turn."""
        memory = self.load_memory()
        memory.append({"user": user_input, "ai": ai_response})
        with open(self.memory_file, "w") as f:
            json.dump(memory, f, indent=4)

    def load_memory(self):
        """Load full conversation memory."""
        with open(self.memory_file, "r") as f:
            memory = json.load(f)
        return memory

    def clear_memory(self):
        """Clear all memory."""
        with open(self.memory_file, "w") as f:
            json.dump([], f)

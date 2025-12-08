# chat_ai.py
from ai_engine.inference import InferenceEngine

class ChatAI:
    """
    Chat system for Etherea: typed input → AI prediction → text output
    """

    def __init__(self, ai_engine=None):
        self.ai_engine = ai_engine
        if not ai_engine:
            raise ValueError("AI engine must be provided for chat system")

    def get_response(self, user_input):
        """Process user input through AI engine and return response."""
        prediction = self.ai_engine.predict(user_input)
        return f"AI response: {prediction:.2f}"

    def chat_loop(self):
        """Start a loop for typed conversation."""
        print("Welcome to Etherea Chat! Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Etherea: Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Etherea: {response}")

# hybrid_interface_memory.py

from ai_engine.sample_model import SampleAI
from ai_engine.preprocessing import Preprocessor
from ai_engine.inference import InferenceEngine
from ai_engine.memory_manager import MemoryManager
from chat_system.chat_ai import ChatAI
from voice_system.commands import VoiceSystem

def setup_ai_engine():
    raw_inputs = ["hello", "world", "etherea", "AI", "focus"]
    targets = [5, 6, 10, 2, 8]
    pre = Preprocessor()
    X = [pre.extract_features(r) for r in raw_inputs]
    ai = SampleAI()
    ai.train(X, targets)
    engine = InferenceEngine(ai)
    return engine

def main():
    engine = setup_ai_engine()
    voice = VoiceSystem(ai_engine=engine)
    chat = ChatAI(ai_engine=engine)
    memory = MemoryManager()

    print("Welcome to Etherea Hybrid Memory Interface!")
    print("Type 'exit' to quit. Speak anytime for voice interaction.\n")

    while True:
        # Voice interaction
        try:
            voice.interact()
        except KeyboardInterrupt:
            print("Voice interaction interrupted. Switching to text input...")

        # Text interaction
        user_input = input("You (text): ")
        if user_input.lower() == "exit":
            print("Etherea: Goodbye!")
            break
        response = chat.get_response(user_input)
        print(f"Etherea: {response}")

        # Save conversation to memory
        memory.add_memory(user_input, response)

if __name__ == "__main__":
    main()
  

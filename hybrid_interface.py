# hybrid_interface.py

from ai_engine.sample_model import SampleAI
from ai_engine.preprocessing import Preprocessor
from ai_engine.inference import InferenceEngine
from chat_system.chat_ai import ChatAI
from voice_system.commands import VoiceSystem

def setup_ai_engine():
    """
    Prepare AI engine with dummy training data.
    """
    raw_inputs = ["hello", "world", "etherea", "AI", "focus"]
    targets = [5, 6, 10, 2, 8]

    pre = Preprocessor()
    X = [pre.extract_features(r) for r in raw_inputs]

    ai = SampleAI()
    ai.train(X, targets)
    engine = InferenceEngine(ai)
    return engine

def main():
    # 1️⃣ Setup AI engine
    engine = setup_ai_engine()

    # 2️⃣ Setup voice system
    voice = VoiceSystem(ai_engine=engine)

    # 3️⃣ Setup chat system
    chat = ChatAI(ai_engine=engine)

    print("Welcome to Etherea Hybrid Interface!")
    print("Type 'exit' to quit text chat. Speak anytime for voice interaction.\n")

    while True:
        # 4️⃣ Voice interaction (non-blocking)
        try:
            voice.interact()
        except KeyboardInterrupt:
            print("Voice interaction interrupted. Switching to text input...")

        # 5️⃣ Text chat interaction
        user_input = input("You (text): ")
        if user_input.lower() == "exit":
            print("Etherea: Goodbye!")
            break
        response = chat.get_response(user_input)
        print(f"Etherea: {response}")

if __name__ == "__main__":
    main()

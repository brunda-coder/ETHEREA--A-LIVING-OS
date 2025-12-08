# chat_test.py
from ai_engine.sample_model import SampleAI
from ai_engine.preprocessing import Preprocessor
from ai_engine.inference import InferenceEngine
from chat_system.chat_ai import ChatAI

# 1️⃣ Prepare dummy dataset
raw_inputs = ["hello", "world", "etherea", "AI", "focus"]
targets = [5, 6, 10, 2, 8]

pre = Preprocessor()
X = [pre.extract_features(r) for r in raw_inputs]

# 2️⃣ Train AI engine
ai = SampleAI()
ai.train(X, targets)
engine = InferenceEngine(ai)

# 3️⃣ Start chat system
chat = ChatAI(ai_engine=engine)
chat.chat_loop()

# inference_test.py
from ai_engine.sample_model import SampleAI
from ai_engine.preprocessing import Preprocessor
from ai_engine.inference import InferenceEngine

# 1️⃣ Prepare dummy dataset
raw_inputs = ["hello", "world", "etherea", "AI", "focus"]
targets = [5, 6, 10, 2, 8]

# 2️⃣ Convert raw inputs to features
pre = Preprocessor()
X = [pre.extract_features(r) for r in raw_inputs]

# 3️⃣ Train sample AI model
ai = SampleAI()
ai.train(X, targets)

# 4️⃣ Save model
ai.save("sample_ai_model")

# 5️⃣ Load model
ai.load("sample_ai_model")

# 6️⃣ Create inference engine
engine = InferenceEngine(ai)

# 7️⃣ Test predictions
test_input = "etherea AI"
prediction = engine.predict(test_input)
print(f"Prediction for '{test_input}': {prediction:.4f}")

from ai_engine.sample_model import SampleAI
from ai_engine.preprocessing import Preprocessor
from voice_system.commands import VoiceSystem
from ai_engine.inference import InferenceEngine

# Prepare AI engine (same as before)
raw_inputs = ["hello", "world", "etherea", "AI", "focus"]
targets = [5, 6, 10, 2, 8]

pre = Preprocessor()
X = [pre.extract_features(r) for r in raw_inputs]
ai = SampleAI()
ai.train(X, targets)
engine = InferenceEngine(ai)

# Start voice interaction
voice = VoiceSystem(ai_engine=engine)
voice.interact()

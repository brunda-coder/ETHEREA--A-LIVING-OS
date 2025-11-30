# Personality Engine Test
from ai_engine.personality_engine import PersonalityEngine

def test_personality_engine():
    engine = PersonalityEngine()
    
    assert engine.current == "balanced"
    assert "natural" in engine.get_system_instruction()

    engine.set_personality("friendly")
    assert engine.current == "friendly"
    assert "warm" in engine.get_system_instruction()

    engine.set_personality("brunda_signature")
    assert "poetic" in engine.get_system_instruction()

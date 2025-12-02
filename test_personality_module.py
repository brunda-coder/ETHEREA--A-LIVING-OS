# MINDFULSCREEN/Etherea Living OS/tests/test_personality_module.py

from ai_engine.personality_engine import PersonalityEngine

def test_personality_engine():
    engine = PersonalityEngine()
    
    # ✅ Check default personality
    assert engine.current == "balanced", "Default personality should be 'balanced'"
    assert "natural" in engine.get_system_instruction(), "Default instructions should contain 'natural'"

    # ✅ Switch to friendly personality
    engine.set_personality("friendly")
    assert engine.current == "friendly", "Personality should be 'friendly'"
    assert "warm" in engine.get_system_instruction(), "Friendly instructions should contain 'warm'"

    # ✅ Switch to Brunda signature personality
    engine.set_personality("brunda_signature")
    assert "poetic" in engine.get_system_instruction(), "Brunda signature instructions should contain 'poetic'"

if __name__ == "__main__":
    # Run the test directly
    test_personality_engine()
    print("All Personality Engine tests passed ✅")

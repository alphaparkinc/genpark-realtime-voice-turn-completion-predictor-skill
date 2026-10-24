import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import RealtimeVoiceTurnCompletionPredictorClient

def main():
    client = RealtimeVoiceTurnCompletionPredictorClient()
    # Case 1: trailing conjunction -> wait
    r1 = client.predict_turn_completion("I need the cordless mop and also", trailing_silence_ms=350)
    print(f"Case 1: Finished={r1['turn_completed_verdict']} -> Action: {r1['recommended_agent_action']}")

    # Case 2: complete question with silence -> trigger
    r2 = client.predict_turn_completion("What is the battery warranty?", trailing_silence_ms=300)
    print(f"Case 2: Finished={r2['turn_completed_verdict']} -> Action: {r2['recommended_agent_action']}")

if __name__ == '__main__':
    main()

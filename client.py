import json
from typing import Dict, Any, Optional

class RealtimeVoiceTurnCompletionPredictorClient:
    """
    Production-grade End-of-Utterance (EoU) and conversational turn completion predictor.
    Combines syntactic clause completeness and trailing silence duration to avoid speech interruptions.
    """
    def __init__(self, silence_threshold_ms: int = 500):
        self.silence_threshold = silence_threshold_ms

    def predict_turn_completion(self, partial_transcript: str = "I would like to order the Roborock vacuum and also", trailing_silence_ms: int = 350) -> Dict[str, Any]:
        p = partial_transcript.strip().lower()

        # Check grammatical unfinished conjunctions
        ends_with_conjunction = any(p.endswith(w) for w in ["and", "or", "but", "because", "also", "so", "with"])
        ends_with_question = p.endswith("?") or any(p.startswith(w) for w in ["what", "how", "when", "can you", "could you"])

        if ends_with_conjunction:
            turn_completed = False
            confidence = 0.90
            action = "WAIT_FOR_USER_CONTINUATION"
        elif trailing_silence_ms >= self.silence_threshold:
            turn_completed = True
            confidence = 0.95
            action = "TRIGGER_AGENT_SPEECH_RESPONSE"
        elif ends_with_question and trailing_silence_ms >= 250:
            turn_completed = True
            confidence = 0.92
            action = "TRIGGER_AGENT_SPEECH_RESPONSE"
        else:
            turn_completed = False
            confidence = 0.70
            action = "BUFFER_AUDIO_LISTENING"

        return {
            "prediction_id": "eou_prd_7719",
            "partial_transcript": partial_transcript,
            "trailing_silence_ms": trailing_silence_ms,
            "ends_with_conjunction": ends_with_conjunction,
            "turn_completed_verdict": turn_completed,
            "prediction_confidence": confidence,
            "recommended_agent_action": action
        }

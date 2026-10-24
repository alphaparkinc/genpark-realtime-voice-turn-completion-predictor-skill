import json, sys
from client import RealtimeVoiceTurnCompletionPredictorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "turn-completion-predictor", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "predict_turn_completion", "description": "Predicts user conversational turn completion and triggers agent speech response."}]}}
    elif method == "tools/call":
        client = RealtimeVoiceTurnCompletionPredictorClient()
        res = client.predict_turn_completion()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = RealtimeVoiceTurnCompletionPredictorClient()
        print(json.dumps(client.predict_turn_completion(), indent=2))

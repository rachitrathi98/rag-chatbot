import json
from pathlib import Path

MEMORY_PATH = Path("../data/memory/chat_history.json")
MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)

def load_memory():
    if MEMORY_PATH.exists():
        return json.loads(MEMORY_PATH.read_text())
    return []

def save_memory(history):
    MEMORY_PATH.write_text(json.dumps(history, indent=2))

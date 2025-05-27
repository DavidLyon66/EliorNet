import uuid
import time
from datetime import datetime
from typing import List, Dict

class ConversationManager:
    def __init__(self):
        self.sessions = {}  # {conversation_id: [messages]}

    def new_conversation_id(self) -> str:
        return str(uuid.uuid4())

    def timestamp(self) -> str:
        return datetime.utcnow().isoformat() + "Z"

    def wrap_message(self, sequence, from_node, to_node, conversation_id=None):
		
        if not conversation_id:
            conversation_id = self.new_conversation_id()

        message = {
            "type": "message",
            "from": from_node,
            "to": to_node,
            "conversation_id": conversation_id,
            "timestamp": self.timestamp(),
            "payload": sequence
        }

        # 👇 Optional: Track it for symbolic reassembly later
        if conversation_id not in self.sessions:
            self.sessions[conversation_id] = []
        self.sessions[conversation_id].append(message)

        return message
    
    def get_conversation(self, conversation_id: str) -> List[Dict]:
        return sorted(self.sessions.get(conversation_id, []), key=lambda x: x["sequence"])

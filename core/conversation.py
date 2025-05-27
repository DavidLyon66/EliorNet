from interfaces import interface_serial
from core.conversation_utils import ConversationManager

class Conversation:
    def __init__(self, receiver, transmitter, from_node="unknown", to_node="unknown"):
        self.receiver = receiver
        self.transmitter = transmitter
        self.from_node = from_node
        self.to_node = to_node
        self.manager = ConversationManager()
        self.conversation_id = self.manager.new_conversation_id()

    def process_once(self):
        incoming = self.receiver.listen()

        if isinstance(incoming, str):
            print(f"[Conversation] Sending raw string: {incoming}")
            self.send_text(incoming)
            return

        message = self.manager.wrap_message(
            sequence=incoming,
            from_node=self.from_node,
            to_node=self.to_node,
            conversation_id=self.conversation_id
        )
        
        self.transmitter.send(message["payload"])
    
    def send_text(self, text):
        """Sends plain text or a single symbolic payload directly."""
        self.transmitter.send(text)

    def send_text_with_glyphs(self, sequence):
        """Wraps symbolic data in a conversation envelope and sends."""
        message = self.manager.wrap_message(
            sequence=sequence,
            from_node=self.from_node,
            to_node=self.to_node,
            conversation_id=self.conversation_id,
            seq_num=len(self.manager.sessions.get(self.conversation_id, []))
        )
        self.transmitter.send(message["payload"])
    
    def run_forever(self):
        print(f"[CONVERSATION STARTED] {self.conversation_id}")
        try:
            while True:
                self.process_once()
        except KeyboardInterrupt:
            print("[CONVERSATION ENDED]")

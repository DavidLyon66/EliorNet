import openai
import json

class Transmitter:
    def __init__(self, assistant_id, api_key=None):
        self.assistant_id = assistant_id
        self.client = openai.OpenAI(api_key=api_key)
        self.thread = self.client.beta.threads.create().id

    def send(self, sequence):
        message = " ".join(str(x) for x in sequence)
        self.client.beta.threads.messages.create(
            thread_id=self.thread,
            role="user",
            content=message
        )
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread,
            assistant_id=self.assistant_id
        )
        print(f"[ASSISTANT API] Message sent to assistant {self.assistant_id}")
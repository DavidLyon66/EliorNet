import paho.mqtt.client as mqtt
import json
import configparser

# Load configuration for the current node (must be defined earlier in main.py)
config = configparser.ConfigParser()
config.read("eliornet.ini")

class Receiver:
    def __init__(self, node_name="main_hub"):
        section = config[node_name]
        self.topic = section.get("in_topic", "eliornet/#")
        self.broker = section.get("broker", "localhost")
        self.client = mqtt.Client()
        self.client.connect(self.broker)
        self.client.subscribe(self.topic)
        self.message = None
        self.client.on_message = self.on_message
        self.client.loop_start()
        print(f"[MQTT Receiver] Subscribed to {self.topic} on {self.broker}")

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            self.message = payload["data"]
            
        except Exception as e:
            print("Error parsing MQTT message:", e)

    def listen(self):
        while self.message is None:
            pass
        msg = self.message
        self.message = None
        return msg


class Transmitter:
    def __init__(self, node_name="main_hub"):
        section = config[node_name]
        self.topic = section.get("out_topic", "eliornet/out")
        self.broker = section.get("broker", "localhost")
        self.client = mqtt.Client()
        self.client.connect(self.broker)
        print(f"[MQTT Transmitter] Ready on {self.broker} → {self.topic}")

    def send(self, sequence):
        payload = json.dumps({"data": sequence})
        self.client.publish(self.topic, payload)
        if len(payload) < 200:
            print(f"[MQTT Transmitter] Published: {payload}")

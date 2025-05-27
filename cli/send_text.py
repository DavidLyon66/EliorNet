import argparse
import configparser
import json
import paho.mqtt.publish as publish
import ast

def main():
    parser = argparse.ArgumentParser(description="Send symbolic message or glyph array via EliorNet MQTT.")
    parser.add_argument("--text", type=str, required=True, help="Message to send (either string or JSON array)")
    parser.add_argument("--from_node", type=str, default="main_hub", help="Node to load config from")
    args = parser.parse_args()

    # Load broker and topic from eliornet.ini
    config = configparser.ConfigParser()
    config.read("eliornet.ini")

    if args.from_node not in config:
        raise ValueError(f"Node '{args.from_node}' not found in config file")

    section = config[args.from_node]
    broker = section.get("broker", "localhost")
    topic = section.get("in_topic", "eliornet/in")

    # Detect if message is a glyph array or string
    message = args.text.strip()
    if message.startswith("[") and message.endswith("]"):
        try:
            data = ast.literal_eval(message)
            if not isinstance(data, list):
                raise ValueError("Input starts with '[', but did not evaluate to a list.")
            payload = {"data": data}
        except Exception as e:
            raise ValueError(f"Failed to parse glyph array: {e}")
    else:
        payload = {"data": message}

    # Send the message
    payload_json = json.dumps(payload)
    print(f"[SEND] Publishing to {broker}:{topic} → {payload_json}")
    publish.single(topic, payload_json, hostname=broker)

if __name__ == "__main__":
    main()

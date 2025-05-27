import argparse
import configparser
import json
import os
import time
from datetime import datetime
import paho.mqtt.client as mqtt

def log_to_file(log_dir, topic, message):
    now = datetime.now()
    logname = f"session-{now.strftime('%Y-%m-%d')}.log"
    log_path = os.path.join(log_dir, logname)

    with open(log_path, "a") as f:
        line = f"[{now.strftime('%H:%M:%S')}] {topic} → {json.dumps(message, indent=2)}\n"
        f.write(line)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[CONNECTED] Subscribing...")
        topic = userdata["mqtt_topic"]
        client.subscribe(topic)
        print(f"[LOGGER] Listening on {userdata['broker']}:{topic} → {userdata['log_dir']}")
    else:
        print(f"[ERROR] Connection failed with code {rc}")

def on_disconnect(client, userdata, rc):
    print(f"[DISCONNECTED] rc={rc}")
    while rc != 0:
        try:
            rc = client.reconnect()
            print("[RECONNECTED]")
        except:
            print("[RECONNECTING...]")
            time.sleep(5)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        data = payload.get("data")

        if isinstance(data, dict) and "content" in data:
            display_data = data.copy()
            display_data["content"] = f"<image content: {data.get('filename', 'hidden')}>"
        else:
            display_data = data

        print(f"[LOG] {msg.topic} → {display_data}")

        if userdata["log_dir"]:
            log_to_file(userdata["log_dir"], msg.topic, display_data)

    except Exception as e:
        print(f"[ERROR] Could not parse message: {e}")

def main():
    parser = argparse.ArgumentParser(description="EliorNet MQTT Symbol Logger")
    parser.add_argument("--config", type=str, default="eliornet.ini", help="Path to config file")
    parser.add_argument("--node", type=str, default="main_hub", help="Section name in config")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    if args.node not in config:
        raise ValueError(f"Node '{args.node}' not found in {args.config}")

    section = config[args.node]
    broker = section.get("broker", "localhost")
    topic = section.get("in_topic", "eliornet/#")
    log_dir = section.get("log_dir", "logs")

    os.makedirs(log_dir, exist_ok=True)

    client = mqtt.Client(userdata={"log_dir": log_dir, "mqtt_topic": topic, "broker": broker})
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.connect(broker)
    client.loop_start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down logger.")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()

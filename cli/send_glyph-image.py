import argparse
import configparser
import json
import base64
import os
import paho.mqtt.publish as publish
from pathlib import Path

MAX_IMAGE_SIZE = 100 * 1024  # 100 KB

def encode_image(filepath):
    ext = filepath.suffix.lower().lstrip(".")
    if ext not in {"svg", "png", "jpg", "jpeg"}:
        raise ValueError("Unsupported image format: must be .svg, .png, .jpg, or .jpeg")

    raw = filepath.read_bytes()
    if len(raw) > MAX_IMAGE_SIZE:
        raise ValueError("Image file too large. Max size is 100 KB.")

    encoded = base64.b64encode(raw).decode("utf-8")
    return ext, encoded

def main():
    parser = argparse.ArgumentParser(description="Send a glyph ID and optional image over EliorNet.")
    parser.add_argument("--glyph", type=int, help="Glyph number (optional if only sending image)")
    parser.add_argument("--to_node", type=str, required=True, help="Target node name (used to construct topic)")
    parser.add_argument("--from_node", type=str, default="main_hub", help="Sender node config")
    parser.add_argument("--image", type=str, help="Optional path to .svg/.png/.jpg image file")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read("eliornet.ini")

    if args.from_node not in config:
        raise ValueError(f"Node '{args.from_node}' not found in eliornet.ini")

    section = config[args.from_node]
    broker = section.get("broker", "localhost")

    topic = f"eliornet/{args.to_node}/in"
    message = {}
    if args.glyph is not None:
        message["glyph"] = args.glyph
    
    if args.image:
        image_path = Path(args.image)
        img_type, img_data = encode_image(image_path)
        message["type"] = img_type
        message["content"] = img_data
        message["filename"] = image_path.name  # short file name only

    payload = {"data": message}
    payload_json = json.dumps(payload)

    print(f"[SEND_GLYPH] Sending to {topic} on {broker} → glyph #{args.glyph} + image: {bool(args.image)}")
    publish.single(topic, payload_json, hostname=broker)

if __name__ == "__main__":
    main()

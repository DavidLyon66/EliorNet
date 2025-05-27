import argparse
import configparser
from core.conversation import Conversation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--from_node", type=str, default="main_hub", help="Name of this node")
    parser.add_argument("--to_node", type=str, default=None, help="Target node name")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    print(f"Starting EliorNet node as: {args.from_node}")

    config = configparser.ConfigParser()
    config.read("eliornet.ini")

    if args.from_node not in config:
        raise ValueError(f"Node '{args.from_node}' not found in config file.")

    node = config[args.from_node]

    to_node = args.to_node or node.get("to_node", "esp32_light")
    if to_node not in config:
        raise ValueError(f"Target node '{to_node}' not found in config file.")

    interface_name = node.get("interface", "mqtt")

    if interface_name == "mqtt":
        from interfaces import interface_mqtt as iface
    elif interface_name == "serial":
        from interfaces import interface_serial as iface
    elif interface_name == "pulse":
        from interfaces import interface_pulse as iface
    else:
        raise ValueError(f"Unsupported interface '{interface_name}'")

    conv = Conversation(
        receiver=iface.Receiver(),
        transmitter=iface.Transmitter(),
    )

    conv.run_forever()

if __name__ == "__main__":
    main()

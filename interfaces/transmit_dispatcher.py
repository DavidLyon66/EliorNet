
from symbolic_utils import format_transmission
import json

def transmit(sequence, mode="text"):
    formatted = format_transmission(sequence, mode)

    if mode == "text":
        message = " ".join(str(part) for part in formatted)
        print("[TEXT] " + message)

    elif mode == "pulse":
        print("[PULSE]")
        for pulse in formatted:
            print(pulse)

    elif mode == "morse":
        print("[MORSE] " + " / ".join(formatted))

    elif mode == "serial":
        raise NotImplemented   
    elif mode == "websockets":

    elif mode == "https":

    else:
        raise ValueError(f"Unsupported mode: {mode}")

# Example usage
if __name__ == "__main__":
    transmit([34, "Hello Elior", 56], mode="text")

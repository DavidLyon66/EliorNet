import serial
import time

class Receiver:
    def __init__(self, port="/dev/ttyUSB0", baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        print(f"[Serial Receiver] Listening on {self.port} at {self.baudrate} baud")

    def listen(self):
        while True:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').strip()
                if line.startswith("[") and line.endswith("]"):
                    try:
                        # Evaluate as a list of values
                        data = eval(line)
                        print(f"[Serial Receiver] Received: {data}")
                        return data
                    except Exception as e:
                        print(f"[Serial Receiver] Failed to parse: {e}")
                else:
                    print(f"[Serial Receiver] Ignored: {line}")


class Transmitter:
    def __init__(self, port="/dev/ttyUSB0", baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        print(f"[Serial Transmitter] Connected to {self.port}")

    def send(self, sequence):
        try:
            msg = str(sequence) + "\n"
            self.ser.write(msg.encode())
            print(f"[Serial Transmitter] Sent: {msg.strip()}")
        except Exception as e:
            print(f"[Serial Transmitter] Failed to send: {e}")

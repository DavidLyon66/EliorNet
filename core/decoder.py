
import cv2
import os
import numpy as np

FRAME_FOLDER = "transmission_frames"
REGION = (98, 98, 60, 60)  # center crop (x, y, w, h)

def analyze_brightness():
    brightness_log = []
    frame_files = sorted([f for f in os.listdir(FRAME_FOLDER) if f.endswith(".png")])
    for frame_file in frame_files:
        path = os.path.join(FRAME_FOLDER, frame_file)
        img = cv2.imread(path)
        x, y, w, h = REGION
        crop = img[y:y+h, x:x+w]
        brightness = np.mean(crop)
        brightness_log.append((frame_file, brightness))
    return brightness_log

def detect_pulses(brightness_log, threshold=50):
    pulses = []
    current_state = None
    for frame, value in brightness_log:
        state = value > threshold
        if state != current_state:
            pulses.append((frame, "ON" if state else "OFF", value))
            current_state = state
    return pulses

if __name__ == "__main__":
    log = analyze_brightness()
    pulses = detect_pulses(log)
    for pulse in pulses:
        print(pulse)

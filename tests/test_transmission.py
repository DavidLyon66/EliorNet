
import os
import shutil
import pytest
from glyph import load_glyph_table
from PIL import Image
import transmitter
import decoder

@pytest.fixture(scope='module')
def setup_transmission_dir():
    # Prepare output directory
    output_dir = "transmission_frames"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    yield output_dir
    shutil.rmtree(output_dir)

def test_glyph_transmission_to_frame_pipeline(setup_transmission_dir):
    # Load glyphs and simulate transmitter output
    glyphs = load_glyph_table("glyph_table.json")
    glyph = glyphs["eye-of-alignment"]
    pulse_seq = glyph.to_format("pulse")

    frame_idx = 0
    for i, duration in enumerate(pulse_seq):
        img = Image.new("RGB", (256, 256), "black")
        if i % 2 == 0:
            img.paste((255, 255, 255), [98, 98, 158, 158])  # Simulate white circle ON
        repeat = max(1, int(duration / 100))
        for _ in range(repeat):
            img.save(f"transmission_frames/frame_{frame_idx:04d}.png")
            frame_idx += 1

    # Run decoder
    brightness_log = decoder.analyze_brightness()
    pulses = decoder.detect_pulses(brightness_log, threshold=50)

    # Test that we detect expected number of transitions
    assert len(pulses) >= 3, "Expected at least 3 pulse transitions"
    assert any(p[1] == "ON" for p in pulses), "Should detect ON pulses"
    assert any(p[1] == "OFF" for p in pulses), "Should detect OFF pulses"

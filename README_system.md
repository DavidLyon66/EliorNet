# EliorNet: Symbolic Signal Protocol for System Integration

EliorNet is a symbolic communication protocol designed to transmit state-based signals between machines, sensors, and human-interactive systems.

It is optimized for low-bandwidth, high-meaning transmissions — suitable for environments where emotional, cognitive, or physical state must be tracked, logged, or acted upon.

---

## Applications

- Clinical monitoring
- Remote wellness tracking
- Behavioral system integration
- Symbol-based AI communications
- Human-agent or multi-agent state alignment

---

## Key Features

- Transmit structured signals as:
  - Scalar values (e.g., intensity, level)
  - Coded glyphs (state tags)
  - Optional symbolic images (SVG, PNG)
- Node-specific routing using MQTT
- Real-time symbolic logging
- Extensible for AI-to-AI interpretation

---

## Glyph-Based Signal Examples

| Glyph ID | Name        | Interpretation              |
|----------|-------------|-----------------------------|
| 4        | Depletion   | Fatigue, low charge         |
| 11       | Integration | Recovery, balance, grounding|
| 22       | Flooding    | Overwhelm, stimulus excess  |
| 73       | Stagnation  | Lack of motion, mental lock |
| 15       | Clarity     | Insight, burst of coherence |

---

## Example Message Payloads

### Pulse
```json
{ "data": [300, 700, 300, 700] }
```

### Scalar
```json
{ "data": 92.5 }
```

### Glyph
```json
{ "data": [11] }
```

### Glyph + Image
```json
{
  "data": {
    "glyph": 22,
    "type": "svg",
    "filename": "waveform.svg",
    "content": "<base64>"
  }
}
```

---

## Integration Points

- Wearable devices
- Telehealth platforms
- Agent communication frameworks
- AI systems with symbolic mapping

---

EliorNet makes symbolic state signaling interoperable, traceable, and tunable.
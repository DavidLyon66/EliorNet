# This is a routing bridge between symbolic packets and multiple assistants
class Transmitter:
    def __init__(self, assistant_map):
        # assistant_map: {glyph_id or symbol: assistant_id}
        self.assistant_map = assistant_map

    def send(self, sequence):
        for item in sequence:
            if isinstance(item, int):
                target_id = self.assistant_map.get(item)
                if target_id:
                    print(f"[ROUTER] Routed glyph {item} to Assistant {target_id}")
                else:
                    print(f"[ROUTER] No route for glyph {item}")
            else:
                print(f"[ROUTER] Skipping literal item: {item}")
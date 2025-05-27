
from glyphs import glyph_table

# Load once at module level
#glyph_table = load_glyph_table("glyph_table.json")

def resolve_element(elem, mode="text"):
    if isinstance(elem, int):
        glyph_id = list(glyph_table.keys())[elem]  # index to ID
        return glyph_table[glyph_id].to_format(mode)
    elif isinstance(elem, str):
        return elem  # keep as-is for text, or apply morse/text conversion here
    elif isinstance(elem, dict):
        return f"[SYS:{elem.get('type', 'unknown')}]"  # placeholder for future system tags
    else:
        return str(elem)

def format_transmission(sequence, mode="text"):
    return [resolve_element(elem, mode) for elem in sequence]

# Example usage
if __name__ == "__main__":
    example = [34, "Hello Elior", 56]
    print("Text Format:", format_transmission(example, "text"))
    print("Pulse Format:", format_transmission(example, "pulse"))

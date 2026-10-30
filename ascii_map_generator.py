"""
ASCII Map Generator & Run-Length Encoder for Ccode.c

This utility provides:
1. Decoding and rendering of the compressed Bangladesh ASCII map string.
2. An encoder that converts any alternating space/asterisk pattern into the
   exact compressed C string format (126 - run_length).
"""

MAGIC_STRING = (
    "y}@z?{|{HtJpy|TgUhQjPlKqIphynJsHw}}JuGwG}}tLmOhXe[`]b[tzn\\tzl]xvn["
    "xwj_}}zvl[}tlOm]}pn_zqmd{}xsmer{|xmfr}zxmfmxm||phwm||z}|{{gwl}WxCxF|y}"
    "="
)

def decode_magic(magic_str: str, line_width: int = 64) -> str:
    """Decodes the run-length encoded magic string into the ASCII map."""
    output = []
    counter = 0

    for i, char in enumerate(magic_str):
        run_length = 126 - ord(char)
        symbol = "*" if (i % 2 == 1) else " "

        for _ in range(run_length):
            output.append(symbol)
            counter += 1
            if counter == line_width:
                output.append("\n")
                counter = 0

    return "".join(output)

def encode_ascii(ascii_art: str, line_width: int = 64) -> str:
    """
    Encodes an ASCII art string (composed of spaces and asterisks)
    into the alternating run-length format: char = chr(126 - count).
    Starts with a space run (even index 0). If the art starts with '*',
    a 0-length space run (chr(126) = '~') is prepended.
    """
    flat = ascii_art.replace("\r", "").replace("\n", "")
    if not flat:
        return ""

    runs = []
    current_char = ' '
    current_count = 0

    for ch in flat:
        target = '*' if ch == '*' else ' '
        if target == current_char:
            current_count += 1
        else:
            runs.append(chr(126 - current_count))
            current_char = target
            current_count = 1

    if current_count > 0:
        runs.append(chr(126 - current_count))

    return "".join(runs)

def main():
    print("=== Bangladesh ASCII Map (Decoded from C magic string) ===")
    decoded = decode_magic(MAGIC_STRING)
    print(decoded)

    # Verify round-trip encoding
    encoded = encode_ascii(decoded)
    print(f"Original length: {len(MAGIC_STRING)} chars | Re-encoded length: {len(encoded)} chars")
    assert decode_magic(encoded) == decoded, "Round-trip assertion failed!"
    print("[OK] Round-trip encode/decode verified successfully.")

if __name__ == "__main__":
    main()

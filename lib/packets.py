import struct

def varint_pack(digit: int) -> bytes:
    out = b''
    while True:
        b = digit & 0x7F
        digit >>= 7
        out += struct.pack("B", b | (0x80 if digit > 0 else 0))
        if digit == 0:
            break
    return out

def varint_unpack(data: bytes) -> tuple:
    d, l = 0, 0
    length = len(data)
    if length > 5:
        length = 5
    for i in range(length):
        l += 1
        b = data[i]
        d |= (b & 0x7F) << 7 * i
        if not b & 0x80:
            break
    return (d, data[l:])


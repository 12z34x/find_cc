"""Decode a Claude thinking `signature` (base64 protobuf envelope).

The signature is a protobuf envelope wrapping an AEAD-encrypted copy of the
model's private reasoning. This module both pretty-prints the structure (CLI)
and exposes `parse_signature()` used by the server to read the *bound model
name* out of the authenticated header (inner field #1 / sub-field #6).

Usage:
    python tools/decode_signature.py <signature-or-@file>
    python tools/decode_signature.py @../replay_out/signature.txt
"""
from __future__ import annotations

import base64
import math
import sys
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional


def _read_varint(buf: bytes, i: int) -> tuple[int, int]:
    shift = val = 0
    while True:
        b = buf[i]
        i += 1
        val |= (b & 0x7F) << shift
        if not b & 0x80:
            return val, i
        shift += 7


def _b64decode(s: str) -> bytes:
    s = s.strip()
    return base64.b64decode(s + "=" * (-len(s) % 4))


def _iter_fields(buf: bytes):
    """Yield (field_number, wire_type, value) for a protobuf message.

    value is an int for varint/i32/i64 and bytes for length-delimited.
    """
    i = 0
    n = len(buf)
    while i < n:
        key, i = _read_varint(buf, i)
        field_no, wt = key >> 3, key & 7
        if wt == 0:
            v, i = _read_varint(buf, i)
            yield field_no, wt, v
        elif wt == 2:
            ln, i = _read_varint(buf, i)
            chunk = buf[i : i + ln]
            i += ln
            yield field_no, wt, chunk
        elif wt == 5:
            yield field_no, wt, buf[i : i + 4]
            i += 4
        elif wt == 1:
            yield field_no, wt, buf[i : i + 8]
            i += 8
        else:  # unknown wire type -> stop
            return


def _get_len_field(buf: bytes, want: int) -> Optional[bytes]:
    for field_no, wt, val in _iter_fields(buf):
        if field_no == want and wt == 2:
            return val
    return None


@dataclass
class SignatureInfo:
    total_bytes: int
    envelope_version: Optional[int]
    model: Optional[str]
    block_type: Optional[str]
    nonce_lengths: list[int] = field(default_factory=list)
    ciphertext_len: int = 0
    ciphertext_entropy: float = 0.0


def _entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    total = len(data)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def parse_signature(signature_b64: str) -> SignatureInfo:
    """Extract structural metadata (incl. the bound model name) from a signature."""
    raw = _b64decode(signature_b64)

    envelope_version = None
    for field_no, wt, val in _iter_fields(raw):
        if field_no == 3 and wt == 0:
            envelope_version = val

    inner = _get_len_field(raw, 2) or b""
    header = _get_len_field(inner, 1) or b""

    model = None
    block_type = None
    for field_no, wt, val in _iter_fields(header):
        if wt == 2 and isinstance(val, (bytes, bytearray)):
            try:
                text = val.decode("utf-8")
            except UnicodeDecodeError:
                continue
            if not text.isprintable():
                continue
            if field_no == 6:
                model = text
            elif field_no == 8:
                block_type = text

    nonce_lengths: list[int] = []
    ciphertext = b""
    for field_no, wt, val in _iter_fields(inner):
        if wt != 2 or not isinstance(val, (bytes, bytearray)):
            continue
        if field_no in (2, 3, 4):
            nonce_lengths.append(len(val))
        elif field_no == 5:
            ciphertext = bytes(val)

    return SignatureInfo(
        total_bytes=len(raw),
        envelope_version=envelope_version,
        model=model,
        block_type=block_type,
        nonce_lengths=nonce_lengths,
        ciphertext_len=len(ciphertext),
        ciphertext_entropy=_entropy(ciphertext),
    )


def _pretty(buf: bytes, depth: int = 0) -> None:
    pad = "  " * depth
    for field_no, wt, val in _iter_fields(buf):
        if wt == 0:
            print(f"{pad}#{field_no} varint = {val}")
        elif wt == 2:
            try:
                text = val.decode("utf-8")
                printable = bool(text) and text.isprintable()
            except UnicodeDecodeError:
                printable = False
            if printable:
                print(f"{pad}#{field_no} len={len(val)} str = {text!r}")
            else:
                head = val[:24].hex()
                more = "…" if len(val) > 24 else ""
                print(f"{pad}#{field_no} len={len(val)} bytes = {head}{more}")
        elif wt == 5:
            print(f"{pad}#{field_no} i32 = {val.hex()}")
        elif wt == 1:
            print(f"{pad}#{field_no} i64 = {val.hex()}")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    arg = argv[1]
    if arg.startswith("@"):
        with open(arg[1:], "r", encoding="utf-8") as fh:
            sig = fh.read()
    else:
        sig = arg

    raw = _b64decode(sig)
    print(f"base64 chars : {len(sig.strip())}")
    print(f"decoded bytes: {len(raw)}")
    print("=== envelope ===")
    _pretty(raw)
    inner = _get_len_field(raw, 2) or b""
    print("=== inner message (field #2) ===")
    _pretty(inner, depth=1)
    header = _get_len_field(inner, 1) or b""
    print("=== header (inner field #1) ===")
    _pretty(header, depth=2)

    info = parse_signature(sig)
    print("=== summary ===")
    print(f"model         : {info.model}")
    print(f"block_type    : {info.block_type}")
    print(f"env version   : {info.envelope_version}")
    print(f"nonce lengths : {info.nonce_lengths}")
    print(
        f"ciphertext    : {info.ciphertext_len} bytes, "
        f"entropy = {info.ciphertext_entropy:.3f} bits/byte"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

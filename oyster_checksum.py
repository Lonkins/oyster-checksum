#!/usr/bin/env python3
"""Compute the 2 Oyster card check digits from the 10-digit prefix.

An Oyster card number is 12 digits: a 10-digit prefix + 2 check digits.
Both check digits are a function of the prefix, so a card with a rubbed-off
or partially-printed number can be recovered from the first 10 digits.

Formula (empirical, from https://seiarotg.me/post/oyster-card-checksum/):

    checksum = (16*N + 3 * sum_{k=0..7} (-1)**k * floor(N / 16**k)) mod 100

where N is the 10-digit prefix as an integer. The result is the last two
digits, zero-padded.

NOTE: the scheme is community-reverse-engineered, not published by TfL.
Verify it against a card whose full number you can read before trusting it.
"""
import sys


def check_digits(prefix: int) -> str:
    """Return the 2 check digits (zero-padded) for a 10-digit prefix."""
    if not 0 <= prefix < 10**10:
        raise ValueError("prefix must be a 10-digit number (0 to 9999999999)")
    s = sum((-1) ** k * (prefix // 16**k) for k in range(8))
    return f"{(16 * prefix + 3 * s) % 100:02d}"


def _digits(s: str) -> str:
    """Strip spaces/dashes, keep digits only."""
    return "".join(c for c in s if c.isdigit())


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: oyster_checksum.py <10-digit prefix | full 12-digit number>")
        return 2

    d = _digits(argv[1])

    if len(d) == 10:
        print(d + check_digits(int(d)))
        return 0

    if len(d) == 12:
        prefix, given = d[:10], d[10:]
        want = check_digits(int(prefix))
        ok = want == given
        print(f"{d}  check digits {'OK' if ok else f'WRONG (expected {want})'}")
        return 0 if ok else 1

    print(f"error: need 10 or 12 digits, got {len(d)}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

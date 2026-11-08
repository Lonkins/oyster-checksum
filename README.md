# oyster-checksum

Recover the last 2 digits of a London Oyster card number from the first 10.

An Oyster card number is **12 digits**: a 10-digit prefix followed by 2 check
digits. Both check digits are a pure function of the prefix, so if the printed
number has worn off or a receipt only shows part of it, the full number can be
reconstructed from the first 10 digits alone.

## Usage

```bash
# compute the full number from a 10-digit prefix
python3 oyster_checksum.py 1234567890
# -> 123456789087

# validate a full 12-digit number
python3 oyster_checksum.py "1234 567890 87"
# -> 123456789087  check digits OK
```

Spaces and dashes in the input are ignored (quote the number if it contains spaces).

## The formula

With `N` as the 10-digit prefix read as an integer:

```
checksum = (16*N + 3 * sum_{k=0..7} (-1)**k * floor(N / 16**k)) mod 100
```

The two check digits are that value, zero-padded.

## Caveat

The scheme is **community reverse-engineered**, not published by Transport for
London — see the original write-up:
<https://seiarotg.me/post/oyster-card-checksum/>. It is empirical and
unverified against TfL's own systems. Before relying on it, test it against a
card whose full 12-digit number you can actually read: if the formula
reproduces that card's real last two digits, it is working.

Intended for recovering **your own** card number. Nothing here reads, decrypts,
or modifies a card.

## Test

```bash
pytest
```

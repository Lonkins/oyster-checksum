from oyster_checksum import check_digits

import pytest


def test_known_card():
    # prefix 1234567890 -> 87
    assert check_digits(1234567890) == "87"


def test_zero_padding():
    # result below 10 must come back two-digit
    assert len(check_digits(0)) == 2


def test_round_trips_through_main_format():
    # full 12-digit number = prefix + its own check digits
    prefix = 1234567890
    assert f"{prefix:010d}" + check_digits(prefix) == "123456789087"


def test_rejects_too_large():
    with pytest.raises(ValueError):
        check_digits(10**10)

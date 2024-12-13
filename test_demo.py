from hypothesis import given
from hypothesis.strategies import text


def encode(s):
    return s.encode("ascii")


def decode(b):
    return b.decode("ascii")


@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s

from hypothesis import given
from hypothesis.strategies import text
from buggy_sort import sort

def encode(s):
    return s.encode("utf-8")

def decode(b):
    return b.decode("utf-8")

@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s

@given(text())
def test_sort_keeps_length(s):
    sorted = sort(s)
    assert len(sorted) == len(s)

@given(text())
def test_is_sorted(s):
    for x, y in zip(s[:-1], s[1:]):
        assert x <= y

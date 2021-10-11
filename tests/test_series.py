from math_series.series import fibonacci
from math_series.series import lucas


def test_fibonacci():
    actual = fibonacci(9)
    excepted = 34
    assert actual == excepted


def test_lucas():
    actual = lucas(9)
    excepted = 76
    assert actual == excepted

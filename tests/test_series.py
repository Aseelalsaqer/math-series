from math_series.series import fibonacci
# from math_series.series import lucas


def test_fibonacci():
    actual = fibonacci(9)
    excepted = 34
    assert actual == excepted

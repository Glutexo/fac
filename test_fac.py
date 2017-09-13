from fac import fac


def test_fac():
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6
    assert fac(4) == 24
    assert fac(5) == 120
    assert fac(10) == 3628800

    assert fac(0) == 1

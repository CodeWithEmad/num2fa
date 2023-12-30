from fractions import Fraction

from num2fa import numbers


def test_non_negative_integer():
    assert numbers(0) == "۰"
    assert numbers(123) == "۱۲۳"
    assert numbers(1000) == "۱۰۰۰"


def test_non_negative_float():
    assert numbers(0.01) == "۰٫۰۱"
    assert numbers(12.345) == "۱۲٫۳۴۵"


def test_negative():
    assert numbers(-1984) == "-۱۹۸۴"
    assert numbers(-19.84) == "-۱۹٫۸۴"
    assert numbers(-123.456, decimal_separator="/") == "-۱۲۳/۴۵۶"
    assert numbers(-123.456, decimal_separator="/", negative="_") == "_۱۲۳/۴۵۶"


def test_decimal_separator():
    assert numbers(123.456, decimal_separator="_") == "۱۲۳_۴۵۶"
    assert numbers(123.456, decimal_separator="٬") == "۱۲۳٬۴۵۶"


def test_fraction_separator():
    assert numbers(Fraction(1, 2), fraction_separator=":") == "۱:۲"
    assert numbers(Fraction(3, 4), fraction_separator="-") == "۳-۴"
    assert numbers(Fraction(5, 7), fraction_separator=".") == "۵.۷"


def test_exponent_numbers():
    assert numbers(1e4) == "۱۰۰۰۰٫۰"
    assert numbers("1e4") == "۱۰۰۰۰٫۰"
    assert numbers("1.1e4") == "۱۱۰۰۰٫۰"
    assert numbers(2e-3) == "۰٫۰۰۲"
    assert numbers("2e-3") == "۰٫۰۰۲"
    assert numbers("2.1e-3") == "۰٫۰۰۲۱"

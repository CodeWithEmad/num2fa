from decimal import Decimal
from fractions import Fraction
from functools import singledispatch
from typing import Union

from num2fa.constants import (
    NUMBERS_DECIMAL_SEPARATOR,
    NUMBERS_FRACTION_SEPARATOR,
    NUMBERS_NEGATIVE,
    PERSIAN_DIGITS,
)
from num2fa.utils import _normalize_str


def _exp_numbers(
    number: str,
    decimal_separator: str,
) -> str:
    # exponent
    base, e, exponent = number.partition("e")
    if exponent:
        return _point_numbers(str(float(number)), decimal_separator)
    return _point_numbers(base, decimal_separator)


def _point_numbers(
    number: str,
    decimal_separator: str,
) -> str:
    before_p, p, after_p = number.partition(".")

    converted = _convert_to_farsi(before_p)
    if after_p:
        converted += decimal_separator + _convert_to_farsi(after_p)
    return converted


def _convert_to_farsi(number: str) -> str:
    """Convert a number to Persian digits."""
    return "".join(PERSIAN_DIGITS.get(digit, digit) for digit in str(number))


@singledispatch
def numbers(
    number: Union[int, float, str, Decimal, Fraction],
    positive: str = "",
    negative: str = NUMBERS_NEGATIVE,
    decimal_separator: str = NUMBERS_DECIMAL_SEPARATOR,
    fraction_separator: str = NUMBERS_FRACTION_SEPARATOR,
) -> str:
    """Return the Persian number string representation of the input number."""
    raise TypeError("Invalid input type for numbers function.")


@numbers.register(str)
@numbers.register(Decimal)
def _(
    number: str,
    positive: str = "",
    negative: str = NUMBERS_NEGATIVE,
    decimal_separator: str = NUMBERS_DECIMAL_SEPARATOR,
    fraction_separator: str = NUMBERS_FRACTION_SEPARATOR,
) -> str:
    # Normalize the number string
    number = _normalize_str(number)

    # sign
    c0 = number[0]
    if c0 == "-":
        sign = negative
        number = number[1:]
    elif c0 == "0":
        sign = ""
    else:
        sign = positive

    numerator, e, denominator = number.partition("/")
    if denominator:
        return (
            sign
            + _point_numbers(numerator, decimal_separator)
            + fraction_separator
            + _point_numbers(denominator, decimal_separator)
        )

    return sign + _exp_numbers(
        numerator,
        decimal_separator,
    )


@numbers.register(int)
@numbers.register(float)
def _(
    number: Union[int, float],
    positive: str = "",
    negative: str = NUMBERS_NEGATIVE,
    decimal_separator: str = NUMBERS_DECIMAL_SEPARATOR,
    fraction_separator: str = NUMBERS_FRACTION_SEPARATOR,
) -> str:
    """Return the Persian number string representation of the input number."""
    return numbers(
        str(number), positive, negative, decimal_separator, fraction_separator
    )


@numbers.register(Fraction)
def _(
    number: Fraction,
    positive: str = "",
    negative: str = NUMBERS_NEGATIVE,
    decimal_separator: str = NUMBERS_DECIMAL_SEPARATOR,
    fraction_separator: str = "/",
) -> str:
    numerator = number.numerator
    denominator = number.denominator
    return (
        numbers(numerator, positive, negative, decimal_separator, fraction_separator)
        + fraction_separator
        + numbers(
            denominator, positive, negative, decimal_separator, fraction_separator
        )
    )


def change_numbers_defaults(
    positive: str = "",
    negative: str = NUMBERS_NEGATIVE,
    decimal_separator: str = NUMBERS_DECIMAL_SEPARATOR,
    fraction_separator: str = NUMBERS_FRACTION_SEPARATOR,
):
    """The the default values for numbers and ordinal_numbers functions."""
    defaults = (
        positive,
        negative,
        decimal_separator,
        fraction_separator,
    )
    change_numbers_defaults.__defaults__ = defaults
    for func in numbers.registry.values():
        func.__defaults__ = defaults
    numbers.__defaults__ = (positive, negative)

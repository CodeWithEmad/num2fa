"""Provide functions to convert a number to Persian words."""

from decimal import Decimal
from fractions import Fraction
from functools import singledispatch
from typing import Union

from num2fa.constants import (
    DEFAULT_SCIENTIFIC_SEPARATOR,
    WORDS_DECIMAL_SEPARATOR,
    WORDS_FRACTION_SEPARATOR,
    WORDS_NEGATIVE,
    ZERO,
)
from num2fa.utils import _natural_words, _normalize_str, _point_words


def _exp_words(
    number: str,
    positive: str,
    negative: str,
    decimal_separator: str,
    scientific_separator: str,
) -> str:
    # exponent
    base, e, exponent = number.partition("e")
    if exponent:
        return (
            _point_words(base, decimal_separator)
            + scientific_separator
            + words(int(exponent), positive, negative)
        )
    return _point_words(base, decimal_separator)


@singledispatch
def words(
    number: Union[int, float, str, Decimal, Fraction],
    positive: str = "",
    negative: str = WORDS_NEGATIVE,
    decimal_separator: str = WORDS_DECIMAL_SEPARATOR,
    fraction_separator: str = WORDS_FRACTION_SEPARATOR,
    ordinal_denominator: bool = True,
    scientific_separator: str = DEFAULT_SCIENTIFIC_SEPARATOR,
) -> str:
    """Return the word form of number.

    If input is a string it should be in the form of a valid Python
    representation for one of the other accepted types. The only exceptions are
    that digits can be in Persian, for example words('۴۲') is valid.

    """
    raise TypeError("invalid input type for words function", number)


@words.register(str)
@words.register(Decimal)
def _(
    number: str,
    positive: str = "",
    negative: str = WORDS_NEGATIVE,
    decimal_separator: str = WORDS_DECIMAL_SEPARATOR,
    fraction_separator: str = WORDS_FRACTION_SEPARATOR,
    ordinal_denominator: bool = True,
    scientific_separator: str = DEFAULT_SCIENTIFIC_SEPARATOR,
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
        if ordinal_denominator:
            return (
                sign
                + _natural_words(numerator)
                + fraction_separator
                + ordinal_words(denominator)
            )
        return (
            sign
            + _natural_words(numerator)
            + fraction_separator
            + _natural_words(denominator)
        )
    return sign + _exp_words(
        numerator,
        positive,
        negative,
        decimal_separator,
        scientific_separator,
    )


@words.register(Fraction)
def _(
    number: Fraction,
    positive: str = "",
    negative: str = WORDS_NEGATIVE,
    decimal_separator: str = WORDS_DECIMAL_SEPARATOR,
    fraction_separator: str = WORDS_FRACTION_SEPARATOR,
    ordinal_denominator: bool = True,
    scientific_separator: str = DEFAULT_SCIENTIFIC_SEPARATOR,
) -> str:
    numerator = number.numerator
    if numerator < 0:
        sign = negative
        numerator = str(numerator)[1:]
    else:
        sign = positive
        numerator = str(numerator)
    if ordinal_denominator:
        return (
            sign
            + _natural_words(numerator)
            + fraction_separator
            + ordinal_words(number.denominator)  # denominator has no sign
        )
    return (
        sign
        + _natural_words(numerator)
        + fraction_separator
        + _natural_words(str(number.denominator))  # denominator has no sign
    )


@words.register(int)
def _(
    number: int,
    positive: str = "",
    negative: str = WORDS_NEGATIVE,
    decimal_separator: str = WORDS_DECIMAL_SEPARATOR,
    fraction_separator: str = WORDS_FRACTION_SEPARATOR,
    ordinal_denominator: bool = True,
    scientific_separator: str = DEFAULT_SCIENTIFIC_SEPARATOR,
) -> str:
    """Return the fa-word form for the given int."""
    if number == 0:
        return ZERO
    if number < 0:
        return negative + _natural_words(str(number)[1:])
    return positive + _natural_words(str(number))


@words.register(float)
def _(
    number: float,
    positive: str = "",
    negative: str = WORDS_NEGATIVE,
    decimal_separator: str = WORDS_DECIMAL_SEPARATOR,
    fraction_separator: str = WORDS_FRACTION_SEPARATOR,
    ordinal_denominator: bool = True,
    scientific_separator: str = DEFAULT_SCIENTIFIC_SEPARATOR,
) -> str:
    """Return the fa-word form for the given float."""
    if number == 0:
        return ZERO
    str_num = str(number)
    if number < 0:
        return negative + _exp_words(
            str_num[1:],
            positive,
            negative,
            decimal_separator,
            scientific_separator,
        )
    return positive + _exp_words(
        str_num,
        positive,
        negative,
        decimal_separator,
        scientific_separator,
    )


def ordinal_words(
    number: Union[int, str],
    positive: str = "",
    negative: str = WORDS_NEGATIVE,
) -> str:
    """Return the number converted to ordinal words form."""
    w = words(int(number), positive, negative)
    if w[-2:] == "سه":
        return w[:-2] + "سوم"
    return w + "م"


def change_words_defaults(
    positive: str = "",
    negative: str = WORDS_NEGATIVE,
    decimal_separator: str = WORDS_DECIMAL_SEPARATOR,
    fraction_separator: str = " ",
    ordinal_denominator: bool = True,
    scientific_separator: str = DEFAULT_SCIENTIFIC_SEPARATOR,
):
    """The the default values for words and ordinal_words functions."""
    defaults = (
        positive,
        negative,
        decimal_separator,
        fraction_separator,
        ordinal_denominator,
        scientific_separator,
    )
    change_words_defaults.__defaults__ = defaults
    for func in words.registry.values():
        func.__defaults__ = defaults
    words.__defaults__ = (positive, negative)

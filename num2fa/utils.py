from num2fa.constants import (
    CLASSES,
    DECIMAL_PLACES,
    HUNDREDS,
    NORMALIZATION_TABLE,
    ONES,
    TEN_TO_TWENTY,
    TENS,
    WORDS_DECIMAL_SEPARATOR,
    ZERO,
)


def _normalize_str(number: str) -> str:
    """Normalize the input number string."""
    return str(number).strip().translate(NORMALIZATION_TABLE)


def _point_words(
    number: str,
    decimal_separator: str,
) -> str:
    before_p, p, after_p = number.partition(".")
    if after_p:
        if before_p == "0":
            if after_p == "0":
                return ZERO
            return _natural_words(after_p) + DECIMAL_PLACES[len(after_p)]
        if after_p != "0":
            return (
                _natural_words(before_p)
                + decimal_separator
                + _natural_words(after_p)
                + DECIMAL_PLACES[len(after_p)]
            )
        return _natural_words(before_p)
    return _natural_words(before_p)


def _natural_words(str_num: str) -> str:
    if str_num == "0":
        return ZERO
    length = len(str_num)
    if length > len(CLASSES) * 3:
        raise ValueError("out of range")

    modulo_3 = length % 3
    if modulo_3:
        str_num = "0" * (3 - modulo_3) + str_num
        length += 3 - modulo_3

    groups = length // 3
    group = groups
    natural_words = ""
    while group > 0:
        three_digit = str_num[group * 3 - 3 : group * 3]
        word3 = _three_digit_words(int(three_digit))
        if word3 and group != groups:
            if natural_words:
                natural_words = (
                    word3
                    + CLASSES[groups - group]
                    + WORDS_DECIMAL_SEPARATOR
                    + natural_words
                )
            else:
                natural_words = word3 + CLASSES[groups - group]
        else:
            natural_words = word3 + natural_words
        group -= 1

    return natural_words


def _three_digit_words(number: int) -> str:
    """Return the word representation of 0 < number < 1000."""
    h, t, o = number // 100, number % 100 // 10, number % 10
    if h == 0 or (t == o == 0):
        w = HUNDREDS[h]
    else:
        w = HUNDREDS[h] + WORDS_DECIMAL_SEPARATOR
    if t == 1:
        return w + TEN_TO_TWENTY[o]
    if o == 0 or t == 0:
        w += TENS[t]
    else:
        w += TENS[t] + WORDS_DECIMAL_SEPARATOR
    return w + ONES[o]

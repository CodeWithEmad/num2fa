from decimal import Decimal
from fractions import Fraction
from math import pi

from num2fa.converters.word_converter import Decimal, Fraction, ordinal_words, words


def test_non_negative():
    """Test the words function."""
    assert words(0) == "صفر"
    assert words("0") == "صفر"
    assert words(1) == "یک"
    assert words(2) == "دو"
    assert words(3) == "سه"
    assert words(4) == "چهار"
    assert words(5) == "پنج"
    assert words(6) == "شش"
    assert words(7) == "هفت"
    assert words(8) == "هشت"
    assert words(9) == "نه"
    assert words(10) == "ده"
    assert words(11) == "یازده"
    assert words(12) == "دوازده"
    assert words(13) == "سیزده"
    assert words(14) == "چهارده"
    assert words(15) == "پانزده"
    assert words(16) == "شانزده"
    assert words(17) == "هفده"
    assert words(18) == "هجده"
    assert words(19) == "نوزده"
    assert words(20) == "بیست"
    assert words(21) == "بیست و یک"
    assert words(22) == "بیست و دو"
    assert words(23) == "بیست و سه"
    assert words(24) == "بیست و چهار"
    assert words(29) == "بیست و نه"
    assert words(30) == "سی"
    assert words(35) == "سی و پنج"
    assert words(44) == "چهل و چهار"
    assert words(57) == "پنجاه و هفت"
    assert words(61) == "شصت و یک"
    assert words(78) == "هفتاد و هشت"
    assert words(80) == "هشتاد"
    assert words(93) == "نود و سه"
    assert words(100) == "یکصد"
    assert words(101) == "یکصد و یک"
    assert words(1235) == "یک هزار و دویست و سی و پنج"
    assert words(99999999) == "نود و نه میلیون و نهصد و نود و نه هزار و نهصد و نود و نه"
    assert (
        words(999999999999999999) == "نهصد و نود و نه بیلیارد"
        " و نهصد و نود و نه بیلیون"
        " و نهصد و نود و نه میلیارد"
        " و نهصد و نود و نه میلیون"
        " و نهصد و نود و نه هزار"
        " و نهصد و نود و نه"
    )


def test_negative_numbers():
    assert ordinal_words(-5) == "منفی پنجم"
    assert words(-5) == "منفی پنج"
    assert words("-5.5") == "منفی پنج و پنج دهم"


def test_non_negative_ordinal_words():
    """Test the ordinal_words function."""
    assert ordinal_words(0) == "صفرم"
    assert ordinal_words("0") == "صفرم"
    assert ordinal_words(1) == "یکم"
    assert ordinal_words(2) == "دوم"
    assert ordinal_words(3) == "سوم"
    assert ordinal_words(4) == "چهارم"
    assert ordinal_words(5) == "پنجم"
    assert ordinal_words(6) == "ششم"
    assert ordinal_words(7) == "هفتم"
    assert ordinal_words(8) == "هشتم"
    assert ordinal_words(9) == "نهم"
    assert ordinal_words(10) == "دهم"
    assert ordinal_words(11) == "یازدهم"
    assert ordinal_words(12) == "دوازدهم"
    assert ordinal_words(13) == "سیزدهم"
    assert ordinal_words(14) == "چهاردهم"
    assert ordinal_words(15) == "پانزدهم"
    assert ordinal_words(16) == "شانزدهم"
    assert ordinal_words(17) == "هفدهم"
    assert ordinal_words(18) == "هجدهم"
    assert ordinal_words(19) == "نوزدهم"
    assert ordinal_words(20) == "بیستم"
    assert ordinal_words(21) == "بیست و یکم"
    assert ordinal_words(22) == "بیست و دوم"
    assert ordinal_words(23) == "بیست و سوم"
    assert ordinal_words(24) == "بیست و چهارم"
    assert ordinal_words(111) == "یکصد و یازدهم"
    assert ordinal_words(1999) == "یک هزار و نهصد و نود و نهم"
    assert ordinal_words(10666) == "ده هزار و ششصد و شصت و ششم"
    assert ordinal_words(999555) == "نهصد و نود و نه هزار و پانصد و پنجاه و پنجم"

    assert ordinal_words(1000000) == "یک میلیونم"


def test_float():
    assert words(0.0) == "صفر"
    assert words("0.0") == "صفر"
    assert words(1.0) == "یک"
    assert words(1.1) == "یک و یک دهم"
    assert words(1.100) == "یک و یک دهم"
    assert words(0.001) == "یک هزارم"
    assert words(0.1001) == "یک هزار و یک ده هزارم"
    assert words(5.45) == "پنج و چهل و پنج صدم"
    assert words(1e-3) == "یک هزارم"
    assert words(1e-3) == "یک هزارم"
    assert words("1e-3") == "یک در ده به توان منفی سه"
    assert words("1E-3") == "یک در ده به توان منفی سه"
    assert words(1e-6) == "یک در ده به توان منفی شش"
    assert words(1e-6) == "یک در ده به توان منفی شش"

    assert words(0.000001) == "یک در ده به توان منفی شش"
    assert words("0.000001") == "یک میلیونم"

    assert words(0.0000011) == "یک و یک دهم در ده به توان منفی شش"
    assert words("0.0000011") == "یازده ده میلیونم"

    assert words(0.00000111) == "یک و یازده صدم در ده به توان منفی شش"

    assert words("0.00000111") == "یکصد و یازده صد میلیونم"

    assert words(0.000001111) == "یک و یکصد و یازده هزارم در ده به توان منفی شش"
    assert words("0.000001111") == "یک هزار و یکصد و یازده میلیاردم"


def test_str_input():
    assert words("42") == "چهل و دو"
    assert words("\t\n 42 \n\t") == "چهل و دو"
    assert words("3.14") == "سه و چهارده صدم"
    assert words("+1.1", positive="مثبت ") == "مثبت یک و یک دهم"
    assert words("1e2") == "یک در ده به توان دو"
    assert words("1E2") == "یک در ده به توان دو"


def test_decimal_input():
    assert words(Decimal("3.0")) == "سه"
    assert words(Decimal("-3.14")) == "منفی سه و چهارده صدم"
    # Let's go beyond floats
    beyond_float = words(Decimal(str(pi) + "238"))
    assert beyond_float != words(pi)
    assert beyond_float.endswith("")
    # Decimal(float('1.1'))
    # == Decimal('1.100000000000000088817841970012523233890533447265625')


def test_fractions():
    assert words(Fraction(16, -10)) == "منفی هشت پنجم"
    assert words(Fraction(Decimal("1.1"))) == "یازده دهم"
    assert words("-8/4") == "منفی هشت چهارم"
    assert words(Fraction(0, 1)) == "صفر یکم"
    assert words("0/1") == "صفر یکم"


def test_persian_numbers():
    assert words("۱") == "یک"
    assert words("۱٫۱") == "یک و یک دهم"
    assert words("۱٬۰۰۰") == "یک هزار"


def test_negative_float():
    assert words(-1.1) == "منفی یک و یک دهم"


def test_positive():
    assert words(0, positive="مثبت ") == "صفر"
    assert words(7, positive="مثبت ") == "مثبت هفت"
    assert words(Fraction("1/2"), positive="مثبت ") == "مثبت یک دوم"
    assert words("1.1e+9", positive="مثبت ") == "مثبت یک و یک دهم در ده به توان مثبت نه"

    assert (
        words(1.1e9, positive="مثبت ") == "مثبت یک میلیارد و یکصد میلیون"
    )  # str(-1.1e+9) == 1100000000.0


def test_negative():
    assert words(-2, negative="منهای ") == "منهای دو"
    assert words("-2", negative="منهای ") == "منهای دو"
    assert words(-1.1, negative="منهای ") == "منهای یک و یک دهم"
    assert words("-1.1", negative="منهای ") == "منهای یک و یک دهم"
    assert (
        words(-1.1e-06, negative="منهای ") == "منهای یک و یک دهم در ده به توان منهای شش"
    )

    assert words("-1/2", negative="منهای ") == "منهای یک دوم"

    assert words(Fraction(1, -2), negative="منهای ") == "منهای یک دوم"


def test_fraction_separator():
    assert (
        words(
            "1/2",
            fraction_separator=" تقسیم بر ",
            ordinal_denominator=False,
        )
        == "یک تقسیم بر دو"
    )
    assert (
        words(
            Fraction(4, -8),
            negative="منهای ",
            fraction_separator=" تقسیم بر ",
            ordinal_denominator=False,
        )
        == "منهای یک تقسیم بر دو"
    )


def test_scientific_separator():
    assert (
        words(1.1e-9, scientific_separator=" ضربدر ده به قوهٔ ")
        == "یک و یک دهم ضربدر ده به قوهٔ منفی نه"
    )

    assert (
        words("1.1e-9", scientific_separator=" ضربدر ده به قوهٔ ")
        == "یک و یک دهم ضربدر ده به قوهٔ منفی نه"
    )


def test_scientific_fraction_separator():
    assert (
        words("1/2", fraction_separator=" تقسیم بر ", ordinal_denominator=False)
        == "یک تقسیم بر دو"
    )

    assert (
        words(
            Fraction(1, 2),
            fraction_separator=" تقسیم بر ",
            ordinal_denominator=False,
        )
        == "یک تقسیم بر دو"
    )

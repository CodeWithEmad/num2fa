""""""


from itertools import chain

PERSIAN_DIGITS = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹",
}

ONES = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]

TENS = ["", "", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]

TEN_TO_TWENTY = [
    "ده",
    "یازده",
    "دوازده",
    "سیزده",
    "چهارده",
    "پانزده",
    "شانزده",
    "هفده",
    "هجده",
    "نوزده",
]

HUNDREDS = [
    "",
    "یکصد",
    "دویست",
    "سیصد",
    "چهارصد",
    "پانصد",
    "ششصد",
    "هفتصد",
    "هشتصد",
    "نهصد",
]

CLASSES = [
    "",
    " هزار",
    " میلیون",
    " میلیارد",
    " بیلیون",
    " بیلیارد",
    " تریلیون",
    " ترلیارد",
    " کوآدریلیون",
    " کادریلیارد",
    " کوینتیلیون",
    " کوانتینیارد",
]

WORDS_NEGATIVE = "منفی "
WORDS_DECIMAL_SEPARATOR = " و "
WORDS_FRACTION_SEPARATOR = " "
NUMBERS_NEGATIVE = "-"
NUMBERS_DECIMAL_SEPARATOR = "٫"
NUMBERS_FRACTION_SEPARATOR = "/"
DEFAULT_SCIENTIFIC_SEPARATOR = " در ده به توان "
ZERO = "صفر"
DECIMAL_PLACES = ["", " دهم", " صدم"]
DECIMAL_PLACES.extend(
    chain.from_iterable(
        (i, " ده" + i, " صد" + i) for i in (i + "م" for i in CLASSES[1:])
    )
)

NORMALIZATION_TABLE = str.maketrans("E٫", "e.", "_٬,+")

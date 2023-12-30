# Num2Fa

[![PyPI releases](https://img.shields.io/pypi/v/num2fa?logo=python&logoColor=white)](https://pypi.python.org/pypi/num2fa)
[![MIT License](https://img.shields.io/github/license/codewithemad/num2fa.svg?style=flat-square)](https://opensource.org/license/agpl-v3/)

`num2fa` is a versatile solution that enables the conversion of numbers (integers, floats, decimals, fractions, or strings) into their corresponding number or word form in Persian.

This repo is built upon the foundation of [num2faword](https://github.com/5j9/num2fawords), and I would like to express my gratitude to the [original developer](https://github.com/5j9) for their contributions.

## Installation

```bash
pip install num2fa
```

That's it!

## Usage

You can use `numbers`, `words`, and `ordinal_words` to convert numbers to their respective Persian forms, whether that be in numeric, word, or ordinal form.

```python
>>> from num2fa import numbers, words, ordinal_words
>>> numbers(1984)
'۱۹۸۴'
>>> numbers('1984')
'۱۹۸۴'
>>> numbers('1.1e-4')
>>> words(1984)
'یک هزار و نهصد و هشتاد و چهار'
>>> ordinal_words(1232)
'یک هزار و دویست و سی و دوم'
>>> ordinal_words(123)
'یکصد و بیست و سوم'
>>> words(1.1e-9)
'یک و یک دهم در ده به توان منفی نه'
```

`numbers` and `words` also accepts other common standard types:

```python

>>> from decimal import Decimal
>>> from fractions import Fraction

>>> numbers(Decimal('1.1'))
'۱٫۱'
>>> numbers(Fraction(-2, 5))
'-۲/۵'
>>> words(Decimal('1.1'))
'یک و یک دهم'
>>> words(Fraction(-2, 5))
'منفی دو پنجم'
>>> ordinal_words(123)
'یکصد و بیست و سوم'
```

## Customization

The default decimal separator for `numbers` is `٫` and for `words` is `و`. it can be changed to any other strings with `decimal_separator`:

```python
>>> numbers(19.75, decimal_separator='/')
'۱۹/۷۵'
>>> words(19.75, decimal_separator=' ممیز ')
'نوزده ممیز هفتاد و پنج صدم'
```

If you wanted to use different number characters for example `٦` instead of `۶`, you can just:

```python
from num2fa.constants import PERSIAN_DIGITS

PERSIAN_DIGITS.update({'6': '٦'})
numbers(19.66, decimal_separator='/')
'۱۹/٦٦'
```

Some people prefer, for example, "صد و هفتاد" over its other form "یکصد و هفتاد". This package uses the second form by default which is also used on official Iranian banknotes. But it can be changed:

```python
>>> from num2fa.constants import HUNDREDS
>>> words(170)
'یکصد و هفتاد'
>>> HUNDREDS[1] = 'صد'
>>> words(170)
'صد و هفتاد'
```

other customizations in `words`:

```python
>>> words(7, positive='مثبت ')
'مثبت هفت'
>>> words(-2, negative='منهای ')
'منهای دو'
>>> words('۱/۲')
'یک دوم'
>>> words('1/2', fraction_separator=' تقسیم بر ', ordinal_denominator=False)
'یک تقسیم بر دو'
>>> words(1.1e-9)
'یک و یک دهم در ده به توان منفی نه'
>>> words(1.1e-9, scientific_separator=' ضربدر ده به قوهٔ ')
'یک و یک دهم ضربدر ده به قوهٔ منفی نه'
```

`positive`, `negative`, `decimal_separator`, `fraction_separator` can be used in `numbers` too.

All above arguments can be used together. If you prefer to change the default argument values once and for all, use the `change_defaults_numbers` or `change_defaults_words` function:

```python
>>> from num2fa import change_numbers_defaults, change_words_defaults

>>> change_numbers_defaults(fraction_separator=' بر ', decimal_separator='.')
>>> numbers('1.89/23')
>>> '۱.۸۹ بر ۲۳'

>>> change_words_defaults(fraction_separator=' بخش بر ', ordinal_denominator=False)
>>> words('۱/۴')
'یک بخش بر چهار'
```

## Contributing

We welcome contributions! To learn how you can contribute, please check the [Contributing](https://github.com/codewithemad/num2fa/blob/master/docs/Contributing.md) document.

## License

This work is licensed under the terms of the [GNU Affero General Public License (AGPL)](https://github.com/codewithemad/num2fa/blob/master/LICENSE.txt).

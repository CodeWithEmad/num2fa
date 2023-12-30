import click

from num2fa.__about__ import __version__
from num2fa.converters.number_converter import numbers
from num2fa.converters.word_converter import ordinal_words, words


class NumberType(click.ParamType):
    name = "number"

    def convert(self, value, param, ctx):
        try:
            if value.startswith("-"):
                return -self.parse_number(value[1:])
            return self.parse_number(value)
        except ValueError:
            self.fail(f"{value} is not a valid number", param, ctx)

    def parse_number(self, value):
        try:
            return int(value)
        except ValueError:
            return float(value)


@click.command(
    help="This command takes a NUMBER as an argument and converts it to Farsi numbers, words or ordinal form depending on the options used:"
)
@click.version_option(version=__version__)
@click.argument("number", type=NumberType())
@click.option("--word", "-w", is_flag=True, help="Convert to Farsi words")
@click.option("--ordinal", "-o", is_flag=True, help="Convert to ordinal from")
def main(number, word, ordinal):
    if ordinal:
        click.echo(ordinal_words(number))
    elif word:
        click.echo(words(number))
    else:
        click.echo(numbers(number))


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter

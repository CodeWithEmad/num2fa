# Development

## Setting up your development environment

Start by cloning the repository:

```bash
git clone https://github.com/codewithemad/num2fa.git
cd num2fa/
```

### Install requirements

```bash
pip install -e ".[dev]"
```

This will install `num2fa` in editable mode with development dependencies.

### Run tests

```bash
make test
```

Yes, there are very few unit tests for now, but this is probably going to change.

## Code formatting

Num2Fa code formatting is enforced by [black](https://black.readthedocs.io/en/stable/). To check whether your code changes conform to formatting standards, run:

make test-format
And to automatically fix formatting errors, run:

```bash
make format
```

Static error detection is performed by [pylint](https://pylint.readthedocs.io/en/latest/). To detect errors, run:

```bash
make test-lint
```

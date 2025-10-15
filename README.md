# Password Generator

A command-line tool to generate secure random passwords with customizable options.

## Features

- Generate random passwords with customizable length
- Include/exclude numbers, symbols, uppercase and lowercase letters
- Command-line interface with easy-to-use options
- Secure random generation using Python's random module

## Usage

```bash
python passgen.py [options]
```

### Options

- `-l, --length` : Set password length (default: 12)
- `-n, --no-numbers` : Exclude numbers
- `-s, --no-symbols` : Exclude symbols
- `-u, --no-uppercase` : Exclude uppercase letters
- `-w, --no-lowercase` : Exclude lowercase letters

### Examples

Generate default password (12 characters, all types included):
```bash
python passgen.py
```

Generate a 16-character password without symbols:
```bash
python passgen.py -l 16 -s
```

Generate password with only lowercase letters and numbers:
```bash
python passgen.py -s -u
```

## Requirements

- Python 3.x
- argparse module (included in Python standard library)

## Installation

1. Clone the repository or download the script
2. Make sure you have Python 3.x installed
3. No additional packages required

## License

This project is open source and available under the MIT License." 

# PassGen - A Secure Password Generator

A simple, secure, and customizable command-line tool for generating cryptographically strong passwords.

## A Note on Security

This tool is built with security as the top priority. Unlike basic password generators that might use Python's standard `random` module (which is not suitable for cryptographic use), PassGen uses the `secrets` module. This ensures that every password is generated with cryptographically secure randomness sourced directly from the operating system's entropy pool, making them unpredictable and safe for use in any security-sensitive application.

## Features

- **Cryptographically Secure:** Utilizes Python's `secrets` module for unpredictable password generation.
- **Highly Customizable:** Control password length and character set composition.
- **Easy to Use:** Clean and intuitive command-line interface.
- **Zero Dependencies:** Runs on any system with Python 3.6+ without needing any external packages.

## Getting Started

Since this tool uses only standard Python libraries, there is no complex installation process.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Hankari-rat/passgen.git
    cd passgen
    ```

2.  **Run the script:**
    ```bash
    python passgen.py [options]
    ```

That's it!

## Usage

### Options

| Option             | Short | Description                                     |
| ------------------ | ----- | ----------------------------------------------- |
| `--length`         | `-l`  | Sets the desired password length (default: 16). |
| `--no-uppercase`   | `-u`  | Excludes uppercase letters (`A-Z`).             |
| `--no-lowercase`   | `-w`  | Excludes lowercase letters (`a-z`).             |
| `--no-numbers`     | `-n`  | Excludes numbers (`0-9`).                       |
| `--no-symbols`     | `-s`  | Excludes symbols (`!@#$%^&*` etc.).             |

### Examples

**1. Generate a default password (16 characters, all types included):**
```bash
python passgen.py
```

**2. Generate a 24-character password without symbols:**
```bash
python passgen.py --length 24 --no-symbols
```
  
**3. Generate a password with only lowercase letters and numbers:**
```bash
python passgen.py --no-uppercase --no-symbols
```
  

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

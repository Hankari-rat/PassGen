import secrets
import string
import argparse

def generate_password(length, use_num, use_sym, use_up, use_low):
    char_pool = ''
    if use_num:
        char_pool += string.digits
    if use_sym:
        char_pool += string.punctuation
    if use_up:
        char_pool += string.ascii_uppercase
    if use_low:
        char_pool += string.ascii_lowercase
    if not char_pool:
        print("At least one character type must be selected. Exiting.")
        return None
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument('-l', '--length', type=int, default=16, help='Length of the password default is 16')
    parser.add_argument('-n', '--no-numbers', action='store_false', help='Exclude numbers from the password')
    parser.add_argument('-s', '--no-symbols', action='store_false', help='Exclude symbols from the password')
    parser.add_argument('-u', '--no-uppercase', action='store_false', help='Exclude uppercase letters from the password')
    parser.add_argument('-w', '--no-lowercase', action='store_false', help='Exclude lowercase letters from the password')
    args = parser.parse_args()
    
    new_password = generate_password(
        length=args.length,
        use_num=args.no_numbers,
        use_sym=args.no_symbols,
        use_up=args.no_uppercase,
        use_low=args.no_lowercase
        )
    print("="*34)
    print("   Random Password Generator   ")
    print("="*34)
    print("[+] Generated password:", new_password)

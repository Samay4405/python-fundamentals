import random
import string

# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# digits = "0123456789"
# symbols = "!@#$%&*"

# character sets
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

all_chars = upper + lower + digits + symbols

length = int(input("Enter password length (>=4): "))

if length < 4:
    print("Password length must be at least 4 to satisfy all character type requirements!")
    print("Conditions (uppercase, lowercase, digits, symbols) cannot apply for length < 4.")
else:
    # # force rule satisfaction
    password_chars = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # remaining characters
    all_chars = upper + lower + digits + symbols
    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))

    # shuffle to remove pattern
    random.shuffle(password_chars)

    # convert list to string
    password = "".join(password_chars)

    print("Generated password:", password)

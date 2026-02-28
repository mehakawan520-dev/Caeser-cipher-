# Caesar Cipher Implementation - Modified Version

def encrypt_message(message, key):
    result = ""

    for ch in message:
        if ch.isalpha():  # Check if character is a letter
            ascii_base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - ascii_base + key) % 26 + ascii_base)
        else:
            result += ch   # Keep special characters unchanged

    return result


def decrypt_message(secret_text, key):
    original = ""

    for ch in secret_text:
        if ch.isalpha():
            ascii_base = 65 if ch.isupper() else 97
            original += chr((ord(ch) - ascii_base - key) % 26 + ascii_base)
        else:
            original += ch

    return original


def main():
    user_text = input("Type your message: ")
    shift_value = int(input("Enter shift number: "))

    cipher_text = encrypt_message(user_text, shift_value)
    print("Cipher Text:", cipher_text)

    plain_text = decrypt_message(cipher_text, shift_value)
    print("Original Text:", plain_text)


if __name__ == "__main__":
    main()
def encrypt_to_hex(text):
    return ''.join(format(ord(char), 'x') for char in text)

def decrypt_from_hex(hex_text):
    return ''.join(chr(int(hex_text[i:i+2], 16)) for i in range(0, len(hex_text), 2))

def encrypt_to_caesar_hex(text, shift=3):
    encrypted = ''.join(chr((ord(char) + shift) % 256) for char in text)
    return ''.join(format(ord(char), 'x') for char in encrypted)

def decrypt_from_caesar_hex(hex_text, shift=3):
    decrypted = ''.join(chr((ord(chr(int(hex_text[i:i+2], 16))) - shift) % 256) for i in range(0, len(hex_text), 2))
    return decrypted
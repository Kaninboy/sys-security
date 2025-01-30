ORIGINAL_TEXT = 'helloworld'
CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'
KEY = 'key'

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_cipher(text, key):
    cipher_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i] in CHARACTERS:
            x = (CHARACTERS.index(text[i]) + CHARACTERS.index(key[i])) % len(CHARACTERS)
            cipher_text.append(CHARACTERS[x])
        else:
            cipher_text.append(text[i])
    return "".join(cipher_text)


ciphered_text = vigenere_cipher(ORIGINAL_TEXT, KEY)
print("Vigenère Ciphered Text:", ciphered_text)
CIPHER_TEXT = 'u my wmzuznak'
CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'
DICT = ['the', 'of', 'and', 'to', 'in', 'that', 'it', 'is', 'was', 'am']

def decrypt_caesar(cipher_text, shift):
    decrypted_text = ''
    for char in cipher_text:
        if char in CHARACTERS:
            index = (CHARACTERS.index(char) - shift) % len(CHARACTERS)
            decrypted_text += CHARACTERS[index]
        else:
            decrypted_text += char
    print(f'Number of shift = {shift}, The decrypted text is : {decrypted_text}')
    return decrypted_text

def brute_force_caesar(cipher_text, dictionary):
    for shift in range(len(CHARACTERS)):
        decrypted_text = decrypt_caesar(cipher_text, shift)
        if any(word in decrypted_text.split() for word in dictionary):
            print(f'The correct shift is {shift}')
            return decrypted_text

brute_force_caesar(CIPHER_TEXT, DICT)
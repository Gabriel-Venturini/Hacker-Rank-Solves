def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    codedString = ''
    for letter in s:
        if letter.lower() in alphabet:
            index = (alphabet.index(letter.lower()) + k) % 26
            if letter.isupper():
                codedString += alphabet[index].upper()
            else:
                codedString += alphabet[index]
        else:
            codedString += letter
    return str(codedString)

# Example usage
plain_text = "abc"
shift = 3
cipher_text = caesarCipher(plain_text, shift)
print(cipher_text)

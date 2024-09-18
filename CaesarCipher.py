def caesar_cipher_encrypt(plaintext, shift): 
    encrypted_text = ""
    for char in plaintext: 
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65) 
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char 
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift): 
    return caesar_cipher_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    plaintext = "Hello, Sabin Ghimire!" 
    shift = 3
    encrypted_text = caesar_cipher_encrypt(plaintext, shift) 
    print("Encrypted:", encrypted_text)
    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift) 
    print("Decrypted:", decrypted_text)

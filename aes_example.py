from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return cipher.iv + ciphertext

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_padded_text, AES.block_size)
    return decrypted_text.decode()

if __name__ == "__main__":
    key = os.urandom(16)
    plaintext = "Hello, AES Sabin!"

    print("Original:", plaintext)

    encrypted_text = aes_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = aes_decrypt(encrypted_text, key)
    print(f"Decrypted: {decrypted_text}")

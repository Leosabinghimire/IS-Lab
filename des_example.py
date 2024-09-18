from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def des_decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = des.decrypt(ciphertext)
    unpadded_text = unpad(decrypted_text, DES.block_size)
    return unpadded_text.decode()
if __name__ == "__main__":
    key = b'8bytekey' 
    plaintext = "Hello, DES Sabin!"
    encrypted_text = des_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted_text}")
    decrypted_text = des_decrypt(encrypted_text, key)
    print(f"Decrypted: {decrypted_text}")

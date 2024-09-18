def generate_key_square(key):

    key = "".join(sorted(set(key), key=key.index))
    key = key.replace("J", "I")  

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    key_square = []
    for char in key:
        if char not in key_square:
            key_square.append(char)
    
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    
    return key_square

def format_plaintext(plaintext):
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = "".join(filter(str.isalpha, plaintext))
    formatted_text = ""
    
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            formatted_text += plaintext[i] + "X"
            i += 1
        elif i + 1 < len(plaintext):
            formatted_text += plaintext[i] + plaintext[i + 1]
            i += 2
        else:
            formatted_text += plaintext[i] + "X"
            i += 1
    
    return formatted_text

def find_position(char, key_square):
    index = key_square.index(char)
    return index // 5, index % 5

def encrypt_pair(pair, key_square):
    r1, c1 = find_position(pair[0], key_square)
    r2, c2 = find_position(pair[1], key_square)
    
    if r1 == r2:
        return key_square[r1 * 5 + (c1 + 1) % 5] + key_square[r2 * 5 + (c2 + 1) % 5]
    elif c1 == c2:
        return key_square[((r1 + 1) % 5) * 5 + c1] + key_square[((r2 + 1) % 5) * 5 + c2]
    else:
        return key_square[r1 * 5 + c2] + key_square[r2 * 5 + c1]

def playfair_encrypt(plaintext, key):
    key_square = generate_key_square(key)
    formatted_text = format_plaintext(plaintext)
    ciphertext = ""
    
    for i in range(0, len(formatted_text), 2):
        ciphertext += encrypt_pair(formatted_text[i:i + 2], key_square)
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_position(ciphertext[i], key_square)
        r2, c2 = find_position(ciphertext[i + 1], key_square)
        
        if r1 == r2:
            plaintext += key_square[r1 * 5 + (c1 - 1) % 5] + key_square[r2 * 5 + (c2 - 1) % 5]
        elif c1 == c2:
            plaintext += key_square[((r1 - 1) % 5) * 5 + c1] + key_square[((r2 - 1) % 5) * 5 + c2]
        else:
            plaintext += key_square[r1 * 5 + c2] + key_square[r2 * 5 + c1]
    
    return plaintext.replace("X", "") 

if __name__ == "__main__":
    key = "MONARCHY"
    plaintext = "INSTRUMENTS"
    
    encrypted_text = playfair_encrypt(plaintext, key)
    decrypted_text = playfair_decrypt(encrypted_text, key)
    
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

import hashlib

def md5_hash(text):
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()

if __name__ == "__main__":
    text = "Hello, MD5 Hashing!"
    hashed_text = md5_hash(text)
    print(f"Original text: {text}")
    print(f"MD5 Hash: {hashed_text}")

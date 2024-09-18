import random

def generate_private_key(p):
    return random.randint(1, p - 1)

def generate_public_key(p, g, private_key):
    return pow(g, private_key, p)

def generate_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

if __name__ == "__main__":
    p = 23
    g = 5

    alice_private = generate_private_key(p)
    alice_public = generate_public_key(p, g, alice_private)

    bob_private = generate_private_key(p)
    bob_public = generate_public_key(p, g, bob_private)

    alice_shared_secret = generate_shared_secret(bob_public, alice_private, p)
    bob_shared_secret = generate_shared_secret(alice_public, bob_private, p)

    print("Alice's Shared Secret:", alice_shared_secret)
    print("Bob's Shared Secret:", bob_shared_secret)

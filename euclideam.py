def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 56
    b = 98
    gcd = euclidean_algorithm(a, b)
    print(f"GCD of {a} and {b} is {gcd}")

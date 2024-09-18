def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

if __name__ == "__main__":
    n = 9
    result = euler_totient(n)
    print(f"Euler's Totient Function of {n} is {result}")

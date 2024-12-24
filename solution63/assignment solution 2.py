def is_prime_all(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

n = int(input("Enter a number: "))
print(f"Is {n} prime? {is_prime_all(n)}")
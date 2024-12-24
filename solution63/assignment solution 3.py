def fibonacci_list_comprehension(n):
    fib_sequence = [0, 1]
    [fib_sequence.append(fib_sequence[-2] + fib_sequence[-1]) for _ in range(2, n)]
    return fib_sequence[:n]

n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence with {n} terms: {fibonacci_list_comprehension(n)}")
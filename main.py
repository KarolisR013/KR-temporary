# fibonacci_script.py

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    count = 20  # Change this value to print more or fewer numbers
    fib_numbers = fibonacci(count)
    print(f"The first {count} Fibonacci numbers are:")
    for i, num in enumerate(fib_numbers):
        print(f"{i + 1}: {num}")

if __name__ == "__main__":
    main()

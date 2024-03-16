def fibonacci_sequence(n):
    sequence = [0, 1]
    
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence[:n]

n = int(input("Enter the number of terms for the Fibonacci sequence: "))

fib_sequence = fibonacci_sequence(n)
print("The Fibonacci sequence up to the", n, "term(s) is:")
print(fib_sequence)
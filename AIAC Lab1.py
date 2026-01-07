#Generate code for the fibonacci sequence up to n terms without functions
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence up to", n, "terms:")
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1


"""# Simplify the code by removing unnecessary variables and conditions. optimze the code 
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to", n, "terms:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

#Generate code for the fibonacci sequence up to n terms with functions
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to", n, "terms:")
    print(' '.join(map(str, fibonacci(n))))

#Give me short report on fibonacci sequence code with and without function
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
usually starting with 0 and 1. The code provided generates the Fibonacci sequence up to 'n' terms in two different ways:
without functions and with functions.

#Fibionacci with iterations and recursion
# Iterative approach
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to", n, "terms (Iterative):")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
print() # for newline  

# Recursive approach
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to", n, "terms (Recursive):")
    print(' '.join(map(str, fibonacci_recursive(n))))
"""
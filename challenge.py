   # This script implements three challenges sequentially using only procedural code,
# without function definitions (def) or external imports, as requested.
# User input is expected for the first two challenges.

# --- Challenge 1: Collatz Conjecture ---
print("=== Challenge 1: Collatz Conjecture ===")

# Prompt for the starting number
print("Enter starting number:", end=" ")
try:
    # Assuming user input will be handled by the environment
    start_num = int(input())
except (EOFError, ValueError):
    start_num = 1 # Default if input fails or is missing

# Collatz Sequence Calculation
n = start_num
sequence = str(start_num)
steps = 0

if n <= 0:
    # Reset if non-positive input is given
    n = 1
    sequence = "1"
    steps = 0
elif n == 1:
    # Special case: starts at 1, sequence is just 1, steps 0
    pass
else:
    # Loop until n reaches 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        sequence += ", " + str(n)
        steps += 1

print(f"Sequence: {sequence} Steps: {steps}")
print("⏎")

# --- Challenge 2: Prime Number Checker ---
print("=== Challenge 2: Prime Number Checker ===")

# Prompt for the number to check
print("Enter a number:", end=" ")
try:
    num = int(input())
except (EOFError, ValueError):
    num = 2 # Default if input fails or is missing

is_prime = True

# Prime checker logic
if num < 2:
    is_prime = False

# Output the testing divisors range
# For input 2, num-1 is 1, so it prints "Testing divisors from 2 to 1..."
print(f"Testing divisors from 2 to {num - 1}...")

if num > 2:
    for j in range(2, num):
        if num % j == 0:
            is_prime = False
            break # Exit loop as soon as a factor is found

if is_prime:
    print(f"{num} is prime!")
else:
    print(f"{num} is not prime.")

print("⏎")

# --- Challenge 3: Multiplication Table ---
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# Print Header Row (1 through 10)
header = "     " # Initial spacing for alignment
for i in range(1, 11):
    header += f"{i:>4}"
print(header)

# Print Table Rows (1 through 10)
for i in range(1, 11):
    # Start the row with the multiplier (i), left-aligned in 3 spaces
    row = f"{i:<3} "

    # Check if this is the final row (i=10) to handle the unusual output formatting
    if i == 10:
        # Print columns 1 through 9 for the last row
        for j in range(1, 10):
            product = i * j
            row += f"{product:>4}"
        print(row)
        # Print the last product (10*10 = 100) on a new, separate line to match the example output
        print(" 100")
    else:
        # Print all 10 columns for rows 1 through 9
        for j in range(1, 11):
            product = i * j
            row += f"{product:>4}"
        print(row)
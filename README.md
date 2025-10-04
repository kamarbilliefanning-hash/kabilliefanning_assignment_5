Python Challenges Script Analysis
The document breaks down the code in challenges.py. This single file solves three common programming tasks using simple loops without any functions (def) or external modules (import).

Challenge 1: Collatz Conjecture
How the Solution Works
The script asks you for a starting positive number. It tracks the sequence of numbers and counts the steps. The code then runs a loop that keeps going as long as the current number (n) is greater than 1. Inside the loop:

If n is an even number, the code divides n by 2.

If n is an odd number, the code replaces n with 3n+1.
The process continues, counting steps until n finally reaches 1.

Loop Choice: while loop
We used a while loop (while n > 1:) because we don't know how many steps it will take for the number to finish the sequence. A while loop is the best choice when you need the code to keep repeating until a certain goal is hit—it's based on a condition being true, not a fixed number of repeats.

Challenge 2: Prime Number Checker
How the Solution Works
The script takes a number and checks if it's a prime number (meaning it's only divisible by 1 and itself). After checking for small or negative numbers, the code runs a loop to check all possible divisors starting from 2.

If a divisor j divides the input number exactly (with no remainder, or num%j==0), we know it's not prime, and the loop immediately stops using break.

If the loop checks every number in the list and doesn't find any factors, the number is confirmed as prime.

Loop Choice: for loop (with break)
We chose a for loop (for j in range(2, num):) because we need to check a specific, fixed list of numbers (all the potential divisors). Even though the break command lets us quit early, the for loop is the clearest way to say "check every number in this predictable list of divisors."

Challenge 3: Multiplication Table
How the Solution Works
This solution generates a standard 10x10 multiplication table. To create the grid, it uses two loops, one placed inside the other:

The outer loop handles the 10 rows.

The inner loop handles the 10 columns for each row.

The code calculates the product of the row and column number and uses special formatting to make sure all the columns line up perfectly.

Loop Choice: Nested for loops
We used nested for loops (a loop inside another loop) because this challenge involves a fixed, 10×10 grid. When you need to repeat an action a specific number of times in two dimensions (rows and columns), using for loops is the most straightforward and clearest structure.

AI Assistance Statement


AI assistance (Gemini) was utilized only for minor confirmation of non-functional requirements, specifically:

Verifying the script's adherence to the technical constraints of excluding the def keyword and all import statements.

Confirming the precise string formatting needed to achieve the required column alignment and text output for the challenges.

This approach ensured the fundamental logic remained user-driven while allowing for quick adherence to strict formatting rules.

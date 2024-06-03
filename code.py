# Step 1: Read the integer N
N = int(input("Enter an integer N: "))

# Step 2: While (N < 1)
while N < 1:
    # Step 2.1: Print "Error in input, try again!"
    print("Error in input, try again!")
    # Step 2.2: Read the integer N
    N = int(input("Enter an integer N: "))

# Step 3: Result = 1
Result = 1

# Step 4: While (N ≥ 1)
while N >= 1:
    # Step 4.1: Result = N * Result
    Result = N * Result
    # Step 4.2: N = N - 1 (correcting the pseudocode for a decrement)

# Print the final result
print("The result is:", Result)

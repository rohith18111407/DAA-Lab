def count_ways(n):
    if n <= 1:
        return 1

    # Create a list to store the number of ways to reach each step
    ways = [0] * (n + 1)

    # Base cases: There is only one way to reach the first and second steps
    ways[1] = 1
    ways[2] = 2

    # Iterate over the remaining steps, building up the solution
    for i in range(3, n + 1):
        # The number of ways to reach the current step is the sum of the ways
        # to reach the previous two steps
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

# Test the implementation
n = 4
result = count_ways(n)
print(f"The number of ways to climb {n} stairs: {result}")

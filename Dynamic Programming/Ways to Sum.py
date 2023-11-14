# Returns the number of arrangements to
# form 'n'
def solve(n):

# Base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    return (solve(n - 1) +
            solve(n - 3) +
            solve(n - 5))

print(solve(6))

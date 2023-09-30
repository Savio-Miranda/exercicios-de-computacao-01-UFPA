def tribonacci(N: int):
    if N <= 1:
        return 0
    elif N == 2:
        return 1
    
    return tribonacci(N - 1) + tribonacci(N - 2) + tribonacci(N - 3)

print(tribonacci(7))

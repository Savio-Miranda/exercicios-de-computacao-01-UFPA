def tribonacci(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

print(tribonacci(0))
print(tribonacci(1))
print(tribonacci(2))
print(tribonacci(6))

"""
tribonacci de 5:
t(4) + t(3) + t(2)
[t(3) + t(2) + t(1)] + [t(2) + t(1) + t(0)] + 1
[1 + 1 + 0] + [1 + 0 + 0] + 1 = 4

tribonacci de 6:
t(5) + t(4) + t(3)
4 + 2 + 1 = 7
"""


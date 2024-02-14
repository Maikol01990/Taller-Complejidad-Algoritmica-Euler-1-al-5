# Problema 1: Multiples of 3 or 5
def problem_1(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

# Problema 2: Even Fibonacci Numbers
def problem_2(limit):
    a, b = 1, 2
    total = 0
    while b < limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

# Problema 3: Largest Prime Factor
def problem_3(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Problema 4: Largest Palindrome Product
def problem_4():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

# Problema 5: Smallest Multiple
def problem_5(n):
    if n == 1:
        return 1
    else:
        from math import gcd
        lcm = 1
        for i in range(1, n + 1):
            lcm = lcm * i // gcd(lcm, i)
        return lcm

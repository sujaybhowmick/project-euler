__author__ = 'sujay'

# #########################################################
# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the
# even-valued terms
# #########################################################


# Loop version
def fibonacci_sum_loop(n):
    x = 1
    y = 1
    z = 1
    even_sum = 0
    for i in range(1, n):
        if z % 2 == 0:
            even_sum += z
        if z > n:
            return even_sum
        z = x + y
        y = x
        x = z
    return even_sum


# Tail Recursive version
def fibonacci_sum_recursion(n):
    def fibonacci_helper(a, b, num, even_sum):
        if b % 2 == 0:
            even_sum += b
        if b > n:
            return even_sum
        return fibonacci_helper(b, a + b, num - 1, even_sum)
    return fibonacci_helper(0, 1, n, 0)

if __name__ == "__main__":
    print fibonacci_sum_loop(4000000)
    print fibonacci_sum_recursion(4000000)

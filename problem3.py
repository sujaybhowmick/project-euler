__author__ = 'sujay'

###############################################################
# What is the largest prime factor of the number 600851475143
###############################################################


def largest_prime(n):
    b = 2
    ld = 1
    while n > 1:
        if n % b == 0:
            if b > ld:
                ld = b
            n /= b
        else:
            b += 1
    return ld

if __name__ == "__main__":
    print largest_prime(600851475143)

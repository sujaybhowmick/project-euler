__author__ = 'sujay'

##########################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
##########################################################################


def print_range():
    for x in range(5, 20, 5):
        print x



def sum_of_multiples_bruteforce():
    sum = 0
    for num in range(1, 1000):
        if num % 3 == 0 or num % 5 == 0:
            sum += num

    return sum


def sum_of_multiples_smarter():
    a = multiples_of_number(3, 999)
    b = multiples_of_number(5, 999)
    c = multiples_of_number(15, 999)

    return (a + b) - c


def multiples_of_number(n, m):
    num_multiples = m / n
    return n * num_multiples * (num_multiples + 1) / 2


if __name__ == "__main__":
    print sum_of_multiples_bruteforce()
    print sum_of_multiples_smarter()

__author__ = 'sujay'

##########################################################################
#Find the largest palindrome made from the product of two n-digit numbers
# Brute force
##########################################################################


def largest_palindrome_bruteforce(num_digits):
    count = (10 ** num_digits) - 1
    largest_palindrome_num = 0
    while count >= 1:
        icount = (10 ** num_digits) - 1
        while icount >= 1:
            num = count * icount

            if is_palindrome(num):
                if num > largest_palindrome_num:
                    largest_palindrome_num = num

            icount -= 1

        count -= 1
    return largest_palindrome_num


def is_palindrome(num):
    num_str = str(num)
    length = len(num_str)

    if length >= 2:

        mid = length / 2

        first_half = num_str[:-mid]
        second_half = num_str[mid:]

        reversed_sh = reverse_num(second_half)

        reversed_fh = reverse_num(first_half)

        reversed_num_str = reversed_sh + reversed_fh

        return num_str == reversed_num_str


def reverse_num(str_num):
    reversed_num = ""
    iterations = len(str_num)
    local_num = int(str_num)

    while iterations > 0:
        reminder = local_num % 10
        local_num /= 10
        reversed_num += str(reminder)

        iterations -= 1
    return reversed_num


if __name__ == "__main__":
    print largest_palindrome_bruteforce(3)
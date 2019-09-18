#############################################################
# FILE : ex7.py
# WRITER : Lautaro Borrovinsky , lautaro , 33783538-3
# EXERCISE : intro2cs ex7 2016-2017
# DESCRIPTION: A program that uses recursive functions in
# order to solve problems like finding out if a number is
# prime or winning at the Hanoi Towers among others
#############################################################


def print_to_n(n):
    """Prints all the integers from 1 to n"""
    if n <= 0:
        return None
    else:
        print_to_n(n - 1), print(n)

print_to_n(0)


def print_reversed(n):
    """Prints all the integers from 1 to n in reverse order"""
    if n <= 0:
        return None
    else:
        print(n), print_to_n(n - 1)


def has_divisor_smaller_than(n, i):
    """Tells if the given number n has divisor/s smaller than
    the given number i"""
    if n == 1:
        return True
    if i == 2:
        return False
    else:
        return (n % (i - 1) == 0) or has_divisor_smaller_than(n, i - 1)


# def has_divisor_smaller_than2(n, i):
#     if n == 1:
#         return True
#     elif i == 2:
#         return False
#     else:
#

def is_prime(n):
    """Tells whether the given number n is or is not prime"""
    bigger_than_sqrt = int(n ** 1 / 2) + 1
    # There will be no number bigger than this that divides n
    if n <= 0:
        print(False)
        # return False
    elif has_divisor_smaller_than(n, bigger_than_sqrt):
        print(False)
        # return False
    else:
        print(True)
        # return True


is_prime(1)
is_prime(7)

def last_divisors(i, f):
    """Returns a list with the divisors of i, which are equal or
    bigger than i"""
    if i < f:
        return []
    if i % f == 0:
        return [f] + last_divisors(i, f + 1)

    return last_divisors(i, f + 1)


def divisors(n):
    """Returns a list with the divisors of n"""
    SMALLER_DIVISOR = 2
    # Smaller possible divisor (different from one) of any number
    # bigger than one
    n = abs(n)
    # For the cases in which n is negative
    if n == 0:
        return []
    if n == 1:
        return [1]
    else:
        return [1] + last_divisors(n, SMALLER_DIVISOR)


def factorial(n):
    """Calculates the factorial of n"""
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def exp_n_x(n, x):
    """returns the sum of the elements of the exponential function"""
    numerator = (x ** n)
    if n == 0:
        return 1
    return numerator / factorial(n) + exp_n_x(n - 1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """Solves the hanoi towers game"""
    if n <= 0:
        return None
    play_hanoi(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n - 1, temp, dest, src)


def binary(n):
    """Returns n binary"""
    if n == "":
        return 1
    elif n == 0:
        return ''
    # The only possibility for n == 0 is ""
    else:
        return binary(n // 2) + str(n % 2)



def bin(x):
    y = 0
    for i in range(len(x)):
        y += int(x[i])*(2**i)
    print (y)

# bin('11010')

def reverse_bin(x):
    return





def print_binary_sequences(n):
    """Prints all the binary sequences of length n"""
    if n == 0:
        print("")
    else:
        for index in range(0, (2 ** n)):
            if len(binary(index)) == n:
                print(binary(index))
            else:
                print(("0" * (n - len(binary(index)))) + str(binary(index)))


def print_sequences_with_prefix(prefix, char_list, n):
    """Prints all the possible sequences of che characters in char_list
    of length n which start with the given prefix"""
    if n == 0:
        print(prefix)
    else:
        for char in char_list:
            print_sequences_with_prefix(char + prefix, char_list, n - 1)


def print_sequences(char_list, n):
    """Prints all the possible sequences of che characters in char_list
    of length n"""
    print_sequences_with_prefix("", char_list, n)


def print_no_rep_sequences_with_prefix(prefix, char_list, n):
    """Prints all the possible sequences of che characters in char_list
    of length n with no repetitions which start with the given prefix"""
    if n == 0:
        print(prefix)
    else:
        for char in char_list:
            if char not in prefix:
                print_no_rep_sequences_with_prefix(prefix + char,
                                                   char_list, n - 1)


def print_no_repetition_sequences(char_list, n):
    """Prints all the possible sequences of che characters in char_list
    of length n with no repetitions"""
    print_no_rep_sequences_with_prefix("", char_list, n)


def no_rep_sequences_with_prefix(prefix, char_list, n, my_list):
    """Returns a list with all the possible sequences of the characters in
    char_list of length n with no repetitions starting with the given prefix"""
    type(my_list) == list
    # The 'recursive equivalent' for creating an empty list in the beginning,
    # if i would create an empty list, the recursion will not fill it
    # on every round
    if n == 0:
        my_list.append(prefix)
    else:
        for char in char_list:
            if char not in prefix:
                no_rep_sequences_with_prefix(prefix + char, char_list, n - 1,
                                             my_list)
    return my_list


def no_repetition_sequences_list(char_list, n):
    """Returns a list with all the possible sequences of the characters in
    char_list of length n with no repetitions"""
    return no_rep_sequences_with_prefix("", char_list, n, [])

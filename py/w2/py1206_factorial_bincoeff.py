# -‐‐-‐--‐-‐‐‐‐‐‐-‐--‐‐‐-‐-‐‐‐‐-‐--‐-‐-‐------‐-‐‐---‐-‐‐‐‐‐‐-‐-‐-‐‐-‐----‐-‐---‐‐-‐------‐-‐‐-‐--‐
#
# 1. Add the function `factorial' which shall accept one argument n. It shall compute n! via
# Algorithm 1 (see Canvas) and return it.
#
# 2. Add the function 'binomialCoefficient' which shall accept two arguments n and k. It shall
# compute 'n choose k'.
#
# ‐‐-‐‐-‐-----‐‐----‐‐-‐‐-‐--‐‐--‐--‐‐‐---‐‐‐‐--‐‐‐--‐‐----‐‐‐---‐‐-‐‐--‐‐-‐--‐--‐‐‐‐--‐‐‐‐‐-‐--‐--
# from fractions import Fraction


def check_n(n=0):
    if not isinstance(n, int) or not n >= 0:
        return False
    else:
        return True


def factorial_recursive(n=0):
    if not check_n(n):
        return None
    int_result = 1
    if n == 0:
        return int_result
    elif n >= 1:
        int_result = n * factorial(n - 1)
        return int_result


def factorial(n=0):
    if not check_n(n):
        return None
    n = int(n)
    i = 1
    int_result = 1
    if n == 0:
        return int_result
    elif n >= 1:
        while i <= n:
            int_result *= i
            i += 1
        else:
            return int_result


def check_k_n(k=0, n=0):
    if (not isinstance(k, int) or not isinstance(n, int)
            or not 0 <= k <= n):
        return False
    else:
        return True


def binomialCoefficient(n=0, k=0):
    if not check_k_n(k, n):
        return None
    else:
        k, n = int(k), int(n)
        # return int(Fraction(factorial(n), factorial(k) * factorial(n - k)))
        return factorial(n) // (factorial(k) * factorial(n - k))


if __name__ == '__main__':
    try:
        k_input = int(input('k = '))
        n_input = int(input('n = '))
    except ValueError:
        print('error')
    print(factorial_recursive(n_input))
    print(factorial(n_input))
    print(binomialCoefficient(n_input, k_input))

# ‐‐‐--‐‐‐-‐-‐‐---‐‐-‐‐-‐‐‐‐----‐--‐---‐‐‐‐‐-‐‐-‐-‐‐-‐--‐-----‐‐‐-‐‐-‐‐‐‐----‐--‐--‐‐‐--‐-‐---‐‐---
#
# Add the definition of a function sumFirstRoots. It shall receive one argument n and use a while-loop
# to return 1^0.5 + 2^0.5 + ... + (n-1)^0.5 + n^0.5, where x^0.5 denotes the square root of x.
#
# --‐‐‐--‐‐‐‐‐‐‐‐--‐-‐-‐‐-‐-‐‐‐‐‐----‐----‐‐‐-‐--‐--‐‐-‐---‐‐‐‐-‐‐‐‐-----‐-‐--‐-‐-‐‐--------‐‐---‐‐
import py1201_add_multiply as py1201


def sumFirstRoots(n=0):
    if isinstance(n, int) and n >= 0:
        x = 1
        result = 0
        while x <= n:
            result += x ** 0.5
            x += 1
        else:
            return result


if __name__ == '__main__':
    error_bool = True
    try:
        n_input = int(input('n = '))
    except ValueError:
        error_bool = False
        print('error')
    if error_bool:
        print(sumFirstRoots(n_input))

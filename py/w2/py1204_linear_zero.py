# -‐‐---‐---‐--‐--‐--‐-‐‐-‐‐‐-‐-‐----‐‐-‐-‐-‐---‐‐---‐‐‐-‐-‐-‐--‐‐‐‐-‐-‐---‐--‐-‐‐-‐‐-‐‐-‐‐‐-‐‐‐--‐
#
# Add code that defines a function linearZero. It shall receive two arguments a, b of type float.
# It shall return the zero of the function y = ax + b, i.e., the value x such that f(x) = 0. If
# the function does not have a zero or if it has infinitely many zeros, then it shall return a
# None object.
#
# ---‐‐--‐‐‐-‐--‐‐-‐‐‐‐‐‐---‐‐----‐-‐‐‐‐‐----‐‐‐-‐--‐---‐‐‐‐-----‐-‐‐‐‐--‐‐‐------‐--‐‐-‐---‐‐--‐‐‐
import py1201_add_multiply as py1201


def linearZero(a=1.0, b=1.0):
    if (py1201.checkInput(a)
        and py1201.checkInput(b)):
        a = float(a)
        b = float(b)
        if a != 0.0 and a != float('inf') and a != float('-inf'):
            return -(b / a)


if __name__ == '__main__':
    error_bool = True
    try:
        a_input = float(input('a = '))
        b_input = float(input('b = '))
    except ValueError:
        error_bool = False
        print('error')
    if error_bool:
        print(linearZero(a_input, b_input))

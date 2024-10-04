# --‐‐‐‐‐--‐‐‐--‐--‐‐‐‐----‐‐---‐---‐---‐‐-‐--‐--‐--‐‐-‐‐-‐--‐‐‐-‐‐‐-‐‐‐--‐‐‐‐----‐‐-‐‐---‐‐-----‐‐
#
# Copy your linearZero function to the file and add code that defines a new function solveForY.
# It has three arguments a, b, y of type float. It first calls linearZero to compute an x such
# that ax + b = 0. Then, it computes an x' such that ax' = y. Finally, it returns x + x',
# such that a (x + x') + b = y. If linearZero returns None, then solveForY also returns None.
#
# --‐‐--‐‐--‐‐‐-‐‐‐‐-‐‐-‐‐---‐-‐‐-‐‐--‐‐‐‐-‐-‐---‐‐-‐‐‐-‐-‐----‐‐--‐--‐-‐‐‐--‐--‐----‐---‐‐--‐‐--‐‐
import py1201_add_multiply as py1201
import py1204_linear_zero as py1204


def solveForY(a=1.0, b=1.0, y=1.0):
    if (py1201.checkInput(a)
        and py1201.checkInput(b)
        and py1201.checkInput(y)):
        a = float(a)
        b = float(b)
        y = float(y)
        x = py1204.linearZero(a, b)
        if x is not None:
            return x + y / a


if __name__ == '__main__':
    error_bool = True
    try:
        a_input = float(input('a = '))
        b_input = float(input('b = '))
        y_input = float(input('y = '))
    except ValueError:
        error_bool = False
        print('error')
    if error_bool:
        print(solveForY(a_input, b_input, y_input))

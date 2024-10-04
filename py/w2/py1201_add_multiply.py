# ‐----‐--‐‐‐--‐-‐--‐-‐--‐-‐---‐-‐‐‐‐‐‐--‐--‐--‐-‐--‐-‐‐-‐‐-‐‐------‐-‐‐‐-‐-‐‐-‐-‐‐-‐-‐‐---‐‐-‐‐‐‐-
#
# Complete the addMultiply function: it shall receive three arguments x, y and z and return xy + z.
#
# -‐--‐‐--‐-‐-‐‐‐--‐----‐-‐---‐---‐‐-‐‐-‐‐-‐---‐‐--‐--‐‐‐-‐--‐--‐--‐‐‐-‐‐‐-‐-‐‐‐‐-‐‐---‐-‐-‐‐--‐‐-‐


def addMultiply(x=0.0, y=0.0, z=0.0):
    if (checkInput(x)
        and checkInput(y)
        and checkInput(z)):
        return x * y + z


def checkInput(input_var):
    if (isinstance(input_var, float)
        or isinstance(input_var, int)
        or isinstance(input_var, bool)):
        return True
    return False


if __name__ == '__main__':
    error_bool = True
    try:
        x_input = float(input('x = '))
        y_input = float(input('y = '))
        z_input = float(input('z = '))
    except ValueError:
        error_bool = False
        print('error')
    if error_bool:
        print(addMultiply(x_input, y_input, z_input))

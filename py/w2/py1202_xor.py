# -‐-‐‐-‐‐‐------‐‐--‐‐-‐‐‐-‐-‐--‐‐-‐-‐--‐--‐‐---‐--‐‐‐--‐‐-‐‐-‐-‐--‐‐-‐-‐---‐--‐‐--‐‐‐‐‐‐---‐--‐-‐
#
# Add code that defines the functions xor2, xor3 and xor4. They shall receive n=2, 3 and 4 bool
# arguments, respectively. Each of them shall return a bool that indicates whether the number of
# arguments that are True is odd. Implement xor3 and xor4 by calling xor2.
#
# ‐‐-‐--‐--‐‐‐‐‐‐-‐-‐‐‐-------‐---‐--‐-‐‐--‐-‐‐‐--‐‐‐---‐-‐‐--‐-‐‐-‐‐‐-‐‐‐‐‐‐‐---‐-‐------‐‐-‐‐-‐--
import py1201_add_multiply as py1201


def xor2(a1=False, a2=False):
    if (py1201.checkInput(a1)
        and py1201.checkInput(a2)):
        if (a1 and not a2) or (not a1 and a2):
            return True
        return False


def xor3(b1=False, b2=False, b3=False):
    if (py1201.checkInput(b1)
        and py1201.checkInput(b2)
        and py1201.checkInput(b3)):
        if xor2(xor2(b1, b2), b3):
            return True
        return False


def xor4(c1=False, c2=False, c3=False, c4=False):
    if (py1201.checkInput(c1)
        and py1201.checkInput(c2)
        and py1201.checkInput(c3)
        and py1201.checkInput(c4)):
        if xor2(xor2(xor2(c1, c2), c3), c4):
            return True
        return False


if __name__ == '__main__':
    error_bool = True
    try:
        list_input = ['a = ', 'b = ', 'c = ', 'd = ']
        for i in range(len(list_input)):
            list_input[i] = input(list_input[i])
            if list_input[i] == 'True':
                list_input[i] = True
            elif list_input[i] == 'False':
                list_input[i] = False
            else:
                list_input[i] = None
    except ValueError:
        error_bool = False
        print('error')
    if error_bool:
        print(xor2(list_input[0],
                   list_input[1]))
        print(xor3(list_input[0],
                   list_input[1],
                   list_input[2]))
        print(xor4(list_input[0],
                   list_input[1],
                   list_input[2],
                   list_input[3]))

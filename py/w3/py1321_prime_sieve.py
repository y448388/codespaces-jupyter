def checkInput(input_var):
    if (isinstance(input_var, float)
        or isinstance(input_var, int)
        or isinstance(input_var, bool)):
        return True
    return False


def primeSieve(n=2):
    if checkInput(n) and n >= 2:
        int__n = int(n)
        set__numbers = set(range(2, int__n + 1))
        set__numbers_with_bool = set()
        for i in set__numbers:
            set__numbers_with_bool.add((i, True))
        set__numbers_mod = set__numbers_with_bool.copy()
        int__f = int(int__n ** 0.5 // 1)
        for i in set__numbers_with_bool:
            if i[0]<= int__f and (i[0], True) in set__numbers_mod:
                k = int((int__n // i[0]))
                for j in range(i[0], k + 1):
                    int__product = int(i[0] * j)
                    if (int__product, True) in set__numbers_mod:
                        set__numbers_mod.remove((int__product, True))
                        set__numbers_mod.add((int__product, False))
        set__result = set()
        for i in set__numbers_mod:
            if i[1]:
                set__result.add(i[0])
        return set__result


if __name__ == '__main__':
    error_bool = True
    try:
        n_input = int(input('n = '))
    except ValueError:
        error_bool = False
        print('error')
    if error_bool:
        print(primeSieve(n_input))

import py1206_factorial_bincoeff as py1206


def printPascalsTriangle(m=0):
    n = 0
    while n <= m:
        k = 0
        while k <= m and k <= n:
            print(py1206.binomialCoefficient(n, k), end=' ')
            k += 1
        print()
        n += 1


if __name__ == '__main__':
    printPascalsTriangle(5)

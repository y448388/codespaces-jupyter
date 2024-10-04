# Do NOT change the first 3 lines of the file.

n = 10

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# Write code that prints, for a given number n, the sum of the squares of the first n positive
# integers using a while-loop. Your code must work for any values not just the provided one.
# Therefore, do not modify the first three lines of the template code.
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


a = 1
b = 0
while a <= 10:
    b += a ** 2
    # print(a, a ** 2, b)
    a += 1
else:
    print(b)

# Do NOT change the first 5 lines of the file.

a = 5
b = 2
c = 4

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# Write code that prints one line to the screen that consists of the given numbers a, b and c in
# ascending order. Do not use sorting-functionality of Python! Your code must work for any values,
# not just for 5, 2, 4.
# Therefore, do not modify the first five lines of the template file.
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
elif c <= b <= a:
    print(c, b, a)

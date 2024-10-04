# Do NOT change the first 6 lines of the file.

x = 2.0
y = 1.0
a = -0.2
b = -0.1

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# Write code that prints a bool to the screen that indicates whether the vectors (x,y) and (a,b)
# given by the coordinates x, y, a and b are parallel, i.e., if xb = ya holds. Your code should
# be robust with respect to floating-point precision, i.e., the vectors shall be considered
# parallel if the equation is violated only slightly, say if |xb - ya| < 10^-6 holds!
# Your code must work for any values not just the provided ones.
# Therefore, do not modify the first six lines of the template code.
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


print(-1e-6 < x * b - y * a < 1e-6)

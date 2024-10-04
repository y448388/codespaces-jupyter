# Do NOT change the first 6 lines of the file.

b1 = 0
b2 = 1
b3 = 0
b4 = 1

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# Write code that prints a bool to the screen that indicates whether the values of b1, b2, b3, b4
# are pairwise distinct, i.e., whether bi = bj only holds for i = j. Your code must work for any
# values, not just 0, 1, 0, 1.
# Therefore, do not modify the first six lines of the template code.
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


print(b1 != b2 and b1 != b3 and b1 != b4 and b2 != b3 and b2 != b4 and b3 != b4)

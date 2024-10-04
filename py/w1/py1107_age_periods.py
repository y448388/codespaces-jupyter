# Do NOT change the first 3 lines of the file.

age = 19

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# Goal: write code that prints, for a given person's age, the number of years until the next
# "age period" begins, which should always be a positive number. We define them to start at the
# ages 0, 5, 18 and 66 for birth, school, full age and retirement, respectively. For an age
# among 0, 5 or 18, print the number of years until the next one to the screen. For an age of 66
# and beyond, print 0 to the screen. Your code must work for any values, not just the age provided
# in the template.
# Therefore, do not modify the first three lines of the template file.
#
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


if 0 <= age < 5:
    print(5 - age)
elif 5 <= age < 18:
    print(18 - age)
elif 18 <= age < 60:
    print(66 - age)
elif age >= 60:
    print(0)
else:
    print(1)

# User enters the number
# number = int(input("Enter number: "))
#
# # checking the number
# if number < 0: print("The entered number is negative.")
# elif number > 0:
#     print("The entered number is positive.")
# elif number == 0:
#     print("Number is zero.")
# else:
#     print("The input is not a number")

# num = 11
# if 9 < num < 99:
#     print("Two digit number")
# elif 99 < num < 999:
#     print("Three digit number")
# elif 999 < num < 9999:
#     print("Four digit number")
# else:
#     print("number is <= 9 or >= 9999")


# i = 1
# j = 5
# while i < 4:
#     while j < 8:
#         print(i, ",", j)
#         j = j + 1
#         i = i + 1

# Python Program to calculate Sum of Series 1²+2²+3²+….+n²

# number = int(input("Please Enter any Positive Number  : "))
# total = 0
#
# total = (number * (number + 1) * (2 * number + 1)) / 6
#
# for i in range(1, number + 1):
#     if (i != number):
#         print("%d^2 + " % i, end=' ')
#     else:
#         print("{0}^2 = {1}".format(i, total))

# Python Program to Print Floyd's Triangle

rows = int(input("Please Enter the total Number of Rows  : "))
number = 1

print("Floyd's Triangle")
i = 1
while(i <= rows):
    j = 1
    while(j <= i):
        print(number, end = '  ')
        number = number + 1
        j = j + 1
    i = i + 1
    print()
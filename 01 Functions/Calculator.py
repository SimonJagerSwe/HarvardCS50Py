# Asking for input
# This reads X and Y as strings and concatenates
# x = input("What's X? ")
# y = input("What's Y? ")
# z = x + y

# print(z)

# Reading as integers
# x = input("What's X? ")
# y = input("What's Y? ")
# z = int(x) + int(y)
# print(z)

# x = int(input("What's X? "))
# y = int(input("What's Y? "))
# print(x + y)

# Working with floating values
# x = float(input("What is X? "))
# y = float(input("What is Y? "))
# z = x + y
# print(z)

# Rounding off
# x = float(input("What is X? "))
# y = float(input("What is Y? "))
# z = round(x + y)
# print(z)

# Using def
def main():
    x = int(input("What's X? "))
    print("x squared is",square(x))

def square(n):
    return n * n
#    return pow(n, 2)           Alternate version


main()
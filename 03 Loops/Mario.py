# Example 1
'''print("#")
print("#")
print("#")'''


# Example 2
'''for _ in range(3):
    print("#")'''


# Example 3
'''def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()'''


# Example 3.1
'''def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()'''


# Example 4
'''def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()'''


# Example 5
'''def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
    # For each brick in row
        for j in range(size):
    # Print brick
            print("#", end="")
        print()

main()'''


# Example 5.1 (cleaner)
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
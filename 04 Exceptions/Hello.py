################### EXCEPTIONS ###################
# Example 0
# Will not work: print("Hello world)
# Will work: print("Hello world!")

# Example 1
'''try:
    x = int(input("What's x? "))
    print(f"x is {x}")

except ValueError:
    print("x is not an integer")'''


# Example 1.1
'''try:
    x = int(input("What is x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")'''


# Example 2
'''while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")'''


# Example 2.1
'''while True:
    try:
        x = int(input("What is x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")'''


# Example 2.2
'''def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break

    return x

main()'''


# Example 2.3
'''def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            print("x is not an integer")


main()'''


# Example 2.4
'''def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass


main()'''


# Example 2.5
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
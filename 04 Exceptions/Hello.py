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
try:
    x = int(input("What is x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
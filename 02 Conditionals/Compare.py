# Example 1 (not recommended)
'''x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
   print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")'''


# Example 2 (better)
'''x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")'''


# Example 3
'''x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")'''


# Example 4
'''x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")

else:
    print("x is equal to y")'''


# Example 4.1
x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")
################ WHILE LOOPS ################
# Example 1 (really bad choice)
'''print("Meow")
print("Meow")
print("Meow")'''


# Example 2
'''i = 3

while i != 0:
    print("Meow")
    i = i-1'''


# Example 3
'''i = 1

while i <= 3:
    print("Meow")
    i = i + 1'''


# Example 4 (always start counting from 0 rather than 1)
'''i = 0

while i < 3:
    print("Meow")
    i += 1          # better shorthand'''



################ FOR LOOPS ################
# Example 1
'''for i in [0, 1, 2]:
    print("Meow")'''


# Example 2
'''for i in range(3):
    print("Meow")'''


# Example 3
'''for _ in range(3):              # Undefined variable not used later
    print("Meow")'''


# Example 4
'''print("Meow"*3)                     # Prints all on the same line'''


# Example 5
'''print("Meow\n"*3)

# Example 5.1
print("Meow\n"*3, end="")'''


# Example 6
'''while True:
    n = int(input("What's n? "))

    if n > 0:
        break

for _ in range(n):
    print("Meow")'''


# Example 7
'''def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("Meow")

main()'''


# Example 8
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()
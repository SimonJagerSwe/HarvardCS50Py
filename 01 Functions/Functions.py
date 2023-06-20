## Hello World
# print("Hello World!")
# print ("Hello World!"       # Will not work

# ARGUMENTS
# Getting input
# v1 (overly complicated)
# print("What's your name? ")
# name = input()
# print("Hello ")

# v2 
# Create value to be returned
# name = input("What's your name? ")
# print("Hello " + name)

# v3 (easiest to read)
# name = input("What's your name? ")
# print(f"Hello {name}")

# Cleaning up the user's mess using .strip
# name = input("What's your name? ")
# name = name.strip()
# name = name.capitalize()          # Only capitalizes the first character
# name = name.title()               # Capitalizes every word
# name = name.strip().title()       # Does both above operations
# name = input("What's your name? ").strip().title()
# print(f"Hello {name}")

# Splitting user name
# name = input("What's your name? ").strip().title()
# first, last = name.split(" ")
# print(f"Hello {first}")


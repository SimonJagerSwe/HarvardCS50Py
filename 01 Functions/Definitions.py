# v1
# def hello(to="world"):
#    print("Hello,", to)
# 
# hello()
# name = input("What's your name? ")
# hello(name)

# v2
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello", to)

main()
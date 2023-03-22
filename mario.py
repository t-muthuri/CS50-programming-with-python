def main():
    print_square(int(input("What's n? ")))

def print_square(size):
    for i in range(size):
        print("#" * size, end="")
        print()

main()
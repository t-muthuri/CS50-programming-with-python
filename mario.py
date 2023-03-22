def main():
    print_square(int(input("What's n? ")))

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
main()
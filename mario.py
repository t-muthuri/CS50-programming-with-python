# stack the blocks 
# method #1
# print("#\n" *3, sep="")

# method #2
# for _ in range(3):
#     print("#")

# method #3
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()
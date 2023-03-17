#ask the person for their name and remove whitespace from str and capitalize person's name
def main():
    name = input ( "What's your name? ")
    hello (name.strip().title())

def hello (to="world"):
    print("hello,", to)

main()
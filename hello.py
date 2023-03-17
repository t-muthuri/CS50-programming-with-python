#ask the person for their name and remove whitespace from str and capitalize person's name
name = input ( "What's your name? ").strip().title()

#split name into first and last name
first, last = name.split(" ")

#say hello to the person
print (f"Hello, {first}")

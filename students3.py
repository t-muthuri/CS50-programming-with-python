class Student:
    def __init__(self, name, house, patronus): #instance variables to objects
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "H"
            case "Otter":
                return "O"
            case "Jack Russell terrier":
                return "JST"
            case _:
                return "/"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input ("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus )

if __name__ == "__main__":
    main()
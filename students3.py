class Student:
    def __init__(self, name, house): #instance variables to objects
        if not name:
            raise ValueError("Missing name")
        self.name = name #instance variable
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #getter-function that gets a value
    @property
    def house(self):
        return self._house #underscore to differentiate between the instance variables and the setter
    
    #setter-function that sets a value
    @house.setter #a decorator
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input ("Name: ")
    house = input("House: ")
    return Student(name, house )

if __name__ == "__main__":
    main()
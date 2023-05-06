class Student:
    def __init__(self, name, house): #instance variables to objects
        if not name:
            raise ValueError
        self.name = name
        self.house = house
    

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input ("Name: ")
    house = input("House: ")
    return Student(name, house) #constructor call-instantiates a student object
    

if __name__ == "__main__":
    main()
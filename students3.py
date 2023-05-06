class Student:
    def __init__(self, name, house): #instance variables to objects
        self.name = name
        self.house = house
    

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input ("Name: ")
    house = input("House: ")
    student = Student(name, house) #constructor call-instantiates a student object
    return student

if __name__ == "__main__":
    main()
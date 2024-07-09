class Student:
    ...


def main():
    student = get_student()
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"
    print(f"{student.name} from {student.house}")


def get_student():
    # student = Student()
    name = input("Name: "),
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()

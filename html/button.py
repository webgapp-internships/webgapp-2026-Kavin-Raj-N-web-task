def get_record(n):

    for i in range(n):
        student = input("Enter Student Name: ")
        students.append(student)
        mark = int(input("Enter Mark: "))
        marks.append(mark)
        dept = input("Enter Department: ")
        department.append(dept)


def calc_rank(marks):
    for j in marks:
        if j < 40:
            ranks.append("F")
        else:
            ranks.append("P")


def print_record(n):
    for k in range(n):
        print("Name: ", students[k])
        print("Mark: ", marks[k])
        print("Dept: ", department[k])
        print("ranks: ", ranks[k], "\n")


students = []
marks = []
department = []
ranks = []
n = int(input("Enter number of students: "))
get_record(n)
calc_rank(marks)
print_record(n)


# Define a class
class Dog:
    """Represents a dog."""

    # Class attribute
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof! Age is {self.age}"


# Create objects (instances)
dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

print(dog1.bark())  # Rex says: Woof!


class print_record:

    def __init__(self, name, mark, dept):
        self.name = name
        self.mark = mark
        self.dept = dept

    def record(self):
        return f"{self.name} got {self.mark} marks and from {self.dept} department"


stu1 = print_record("Eris", 35, "IT")
stu2 = print_record("Hanna", 40, "CS")

print(stu1.record())
print(stu2.record())

# Parent class
class Parent:
    def _init_(self, father_name, mother_name):
        self.__father_name = father_name   # private attribute
        self.__mother_name = mother_name   # private attribute

    # Getter methods
    def get_father_name(self):
        return self.__father_name

    def get_mother_name(self):
        return self.__mother_name

    # Setter methods
    def set_father_name(self, father_name):
        self.__father_name = father_name

    def set_mother_name(self, mother_name):
        self.__mother_name = mother_name


# Child class inheriting Parent
class Student(Parent):
    def __init__(self, student_name, roll_no, father_name, mother_name):
        super()._init_(father_name, mother_name)
        self.__student_name = student_name
        self.__roll_no = roll_no

    # Getter methods
    def get_student_name(self):
        return self.__student_name

    def get_roll_no(self):
        return self.__roll_no

    # Setter methods
    def set_student_name(self, student_name):
        self.__student_name = student_name

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def display_details(self):
        print("Student Name:", self.get_student_name())
        print("Roll No:", self.get_roll_no())
        print("Father's Name:", self.get_father_name())
        print("Mother's Name:", self.get_mother_name())


# Creating object
s1 = Student("Rubina Maharjan", 101, "Nanibabu Maharjan", "Ramila Maharjan")

# Display details
s1.display_details()

# Modifying data using setter methods
s1.set_student_name("Nishesh Maharjan")
s1.set_roll_no(102)

print("\nAfter Updating:")
s1.display_details()
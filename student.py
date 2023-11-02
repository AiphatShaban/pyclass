from tuitions import Payment

class Student:
    # class attributes
   
    students = []

    def __init__(self, name, age, fees):
        self.name = name
        self.age = age
        self.fees = Payment(self, fees)
        Student.students.append(self)

    def __str__(self):
        return f'Name : {self.name}\nAge: {self.age}\n{self.fees}'

    def get_fees(self):
        return self.fees
    

    def get_all_students(self):
        return self.students
   




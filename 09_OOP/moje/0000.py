class Student:

    university_name = 'New York Academy'

    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age


    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

obj_anna = Student('anna', 'kowalska', 23)
obj_arek = Student('arkadiusz', 'nowak', 25)

print(obj_anna.email())
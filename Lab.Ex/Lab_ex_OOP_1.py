class Person:
    def __int__(self, name, family_name, age, nationality):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.nationality = nationality

    def print(self):
        print("First name: ", self.name,
              "| Last name: ", self.family_name,
              "| Nationality: ", self.nationality)


class Student(Person):
    def __int__(self, name, family_name, age, nationality, university, year_of_study):
        super().__int__(name, family_name, age, nationality)
        self.university = university
        self.year_of_study = int(year_of_study)

    def print(self):
        print("First name: ", self.name,
              "| Last name: ", self.family_name,
              "| Nationality: ", self.nationality,
              "| University: ", self.university,
              "| Year of enrollment: ", self.year_of_study)


class Lecturer(Person):
    def __int__(self, name, family_name, age, nationality, university, experience):
        super().__int__(name, family_name, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print("First name: ", self.name,
              "| Last name: ", self.family_name,
              "| Nationality: ", self.nationality,
              "| University: ", self.university,
              "| Years of experience: ", self.experience)


class ReverseString():
    user_input = input("Enter text: ")

    def __int__(self, user_input):
        self.user_input = user_input

    def reverse(self):
        for el in range(len(self.user_input)-1, -1, -1):
            print(self.user_input[el])


obj1 = Person()
obj1.name = "Ivan"
obj1.family_name = "Ivanov"
obj1.age = 32
obj1.nationality = "Bulgarian"
obj1.print()

obj2 = Student()
obj2.name = "Zara"
obj2.family_name = "Antova"
obj2.age = 47
obj2.nationality = "Bulgarian"
obj2.university = "Technical University of Sofia"
obj2.year_of_study = 1991
obj2.print()

obj3 = Lecturer()
obj3.name = "Daniela"
obj3.family_name = "Gotseva"
obj3.age = "N/A"
obj3.nationality = "Bulgarian"
obj3.university = "Technical University of Sofia"
obj3.experience = "N/A"
obj3.print()

obj4 = ReverseString()
obj4.reverse()

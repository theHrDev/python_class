class Person:
    name="Rukayat"
    dept ="CSC"
    def __init__(self):
        print("This is the contructor")
        
    def greetUser(self):
        print(f"Hello {self.name}")
    
    def userInfo(self,age):
        print(f"Hi {self.name}, you are in {self.dept} department and you are {age} years old")
    
    
# Person() self in this case is referring to the object that is about to create
person_1 = Person()
# print(person_1)
print(person_1.name)
print(person_1.greetUser())
print(person_1.userInfo(3))



# color = "red"
# name = "Taye"
# dept = "CSC"
class Person:
    def __init__(self, new_name, new_dept):
        self.name = new_name
        self.dept = new_dept
        print(self.name, self.dept)
        self.greet()


    def say_hi(self):
        print(f"{self.name} How are you doing today?")
    
    def change_name(self, new_name):
        self.name = new_name
    
    def greet(self):
        print("Good evening everyone")


Person("Tolu", "BCH")
person_2 = Person("Ajayi", "PSG")
# print(person_1.name)
    
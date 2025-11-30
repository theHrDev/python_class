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
    
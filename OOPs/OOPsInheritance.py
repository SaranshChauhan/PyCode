class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("I am {0} and my age is {1} years.".format(self.name,self.age))        

    def speak(self): #This method will be overridden by both Cat & Dog method's Speak
        print("I don't speak any language!")

class Cat(Pet): #inherit the Pet Class
   def speak(self):
       print("Meow")
class Dog(Pet):
    def speak(self):
        print("Bark")

obj1 = Cat("Cat",20)
obj1.speak()
obj1.show()

obj2 = Dog("Dog",18)
obj2.speak()
obj2.show()
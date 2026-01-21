# Simple Inheritance
# class A:
#     def __init__(self,name):
#         self.name = name
#     def call(self):
#         print(f"parent call {self.name}")

# class B(A):

#     def B_call(self):
#         print(f"inside b {self.name}")

# b = B("sdf")
# b.B_call()

# # Multi-level Inheritance
# class A:
#     def __init__(self,name):
#         self.name = name
#     def call(self):
#         print(f"parent call {self.name}")

# class B(A):

#     def B_call(self):
#         print(f"inside b: {self.name}")

# class C(B):
#     def C_call(self):
#         print(f"inside c: {self.name}")

# c = C("sdf")
# c.C_call()


# # Heirarichal Inheritance
# class A:
#     def __init__(self,name):
#         self.name = name
#     def call(self):
#         print(f"parent call {self.name}")

# class B(A):

#     def B_call(self):
#         print(f"inside b: {self.name}")

# class C(A):
#     def C_call(self):
#         print(f"inside c: {self.name}")

# c = C("sdf")
# c.C_call()

# # Multiple Inheritance
# class A:
#     def __init__(self,name):
#         self.name = name
#     def call(self):
#         print(f"parent call {self.name}")

# class B(A):

#     def B_call(self):
#         print(f"inside b: {self.name}")

# class C(A):
#     def C_call(self):
#         print(f"inside c: {self.name}")

# class D(B,C):
#     def D_call(self):
#         print(f"inside d: {self.name}")


# d = D("sdf")
# d.D_call()



#Hybrid Inheritance

#Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.

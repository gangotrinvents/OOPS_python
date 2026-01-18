# initiate a class
class mobile:
    # special method/magic method/dunder method - construction (after def type _)
    def __init__(self):
        self.name = 'Vivo'
        self.model = 'V40'
        self.space = '256 GB'
    
    def call(self, cll):
        print(f"Call came from {cll}")

mob = mobile()

#printing attribute
print(mob.model)

#calling a method
mob.call("Ram")

# our object is class
print(type(mob))

# basics done
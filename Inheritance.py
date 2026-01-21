class animal: # parent
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makess a sound.")

class dog(animal): #child

    def __init__(self,breed):
        super().__init__()
        self.breed == breed
    def speak1(self):
        print(f"{self.name} is barking")

# a = animal("dog")
# a.speak()

d = dog("Dog")
d.speak1()
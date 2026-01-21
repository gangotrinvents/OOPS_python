class animal: # parent
    def __init__(self):
        self.name = "Ram"

class dog(animal): #child
    def __init__(self,breed):
        # super().__init__()
        self.breed = breed

d = dog("Pav")
print(d.breed)
print(d.name)
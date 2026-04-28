
class Mammal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Human(Mammal):
    def __init__(self, name: str, age: int, surmame: str, address: str, ):
        super().__init__(name, age)
        self.surname = surmame
        self.address = address

    def get_age(self):
        return self.age
    

class Dog(Mammal):
    def __init__(self, name: str, age: int, owner: str | None):
        super().__init__(name, age)
        self.owner = owner

    def get_age(self):
        if self.age == 1:
            return 15
        if self.age == 2:
            return 24
        if self.age > 2:
            return 24 + (self.age - 2) * 4
        

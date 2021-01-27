class Student:
    def __init__(self, id, name, lastname):
        self.id = id
        self.name = name
        self.lastname = lastname
    
    def __str__(self):
        return f"{self.id} {self.name} {self.surname}"
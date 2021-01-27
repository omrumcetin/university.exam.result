class University:
    def __init__(self, id, name, base_point, capacity):
        self.id = id
        self.name = name
        self.base_point = base_point
        self.capacity = capacity
    
    def __str__(self):
        return f"{self.id},{self.name},{self.base_point},{self.capacity}"
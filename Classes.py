class Loot:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
class Piece:
    def __init__(self, type, location, color):
        self.type = type
        self.location = location
        self.color = color

    def __str__(self):
        return f"{self.type} {self.location} is {self.color}"

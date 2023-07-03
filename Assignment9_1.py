
class MathOperations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print("Addition: ",self.x + self.y)

    def sub(self):
        print("Subtraction: ",self.x - self.y)

    def mul(self):
        print("Multiplication: ",self.x * self.y)

    def div(self):
        if self.y == 0:
            raise ZeroDivisionError
        print("Division: ",self.x / self.y)

    def pow(self):
        print("Power: ",self.x ** self.y)
        
    def floorDiv(self):
        print("Floor Division: ",self.x // self.y)


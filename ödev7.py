import math

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, diger):
        return Vektor(self.x + diger.x, self.y + diger.y)

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __len__(self):
        return round(abs(self))


if __name__ == "__main__":
    v1 = Vektor(3, 4)
    v2 = Vektor(1, 2)

    print(v1)             
    print(v2)             

    v3 = v1 + v2           
    print(v3)             

    print(abs(v1))         
    print(len(v1))         
    print(len(v3))         
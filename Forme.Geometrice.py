import math


# Clasa de baza Shape
class Shape:
    def area(self):
        raise NotImplementedError("Aceasta metodă trebuie să fie implementată în clasele derivate.")

    def __str__(self):
        return "Formă geometrică"


# Clasa Circle care moștenește din Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area():.2f}"


# Clasa Rectangle care moștenește din Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"


# Functie de intrare date de la tastatura
def input_data():
    # Alegem să citim valorile pentru cerc și dreptunghi
    shape_type = input("Alegeți forma (circle sau rectangle): ").lower()

    if shape_type == 'circle':
        radius = float(input("Introduceți raza cercului: "))
        circle = Circle(radius)
        print(circle)

    elif shape_type == 'rectangle':
        width = float(input("Introduceți lățimea dreptunghiului: "))
        height = float(input("Introduceți înălțimea dreptunghiului: "))
        rectangle = Rectangle(width, height)
        print(rectangle)

    else:
        print("Forma nu este validă. Alegeți 'circle' sau 'rectangle'.")


# Apelarea funcției pentru a începe programul
input_data()


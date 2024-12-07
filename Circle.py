"""

Create a Python Class called Circle with constructor which will take a
list as an argument for the task. The list is
[10,501,22,37,100, 998,87, 351]

"""
class circle:
    Pi=3.14
    # Instance attribute
    def __init__(self, radius):
        self.radius=radius

    #Calculate Perimeter
    def Perimeter(self):
        for i in self.radius:
            circle_perimeter=self.Pi *i *2
            print("Perimeter is", circle_perimeter)

    #Calculate Area
    def Area(self):
        for i in self.radius:
            circle_area=self.Pi * i * i
            print("Area is", circle_area)
            
# Driver code
# Object instantiation
Radius=[10,501,22,37,100, 998,87, 351]
circle1 = circle(Radius)

# Accessing class attributes
print("Radius of Circles are", circle1.radius)
circle1.Area()
circle1.Perimeter()


import Shape

circle = Shape.Circle(0,1,"Blue",9)
rectangle = Shape.Rectangle(1,0,"White",14,9)
triangle = Shape.Triangle(0,0,"Black",5,6,7)

print("Circle\n Area: {} \n Perimeter: {}".format(circle.getArea(),circle.getPerimeter()))
print("\nRectangle\n Area: {} \n Perimeter: {}".format(rectangle.getArea(),rectangle.getPerimeter()))
print("\nTriangle\n Area: {} \n Perimeter: {}".format(triangle.getArea(),triangle.getPerimeter()))
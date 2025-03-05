class Figure():
    unit = "cm"
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Square(Figure):
    def __init__(self,side_lenght):
        super().__init__()
        self.__side_lenght = side_lenght
    def calculate_area(self):
        return self.__side_lenght ** 2

    def info(self):
        return f'Square side lenght: {self.__side_lenght}cm , area:{self.calculate_area()}cm'
class Rectangle(Figure):
    def __init__(self,lenght,width):
        super().__init__()
        self.__lenght = lenght
        self.__width = width
    def calculate_area(self):
        return self.__lenght * self.__width
    def info(self):
        return f'Rectangle lenght: {self.__lenght}cm, width: {self.__width}cm . Area : {self.calculate_area()}'


rectangle = Rectangle(12,2)
rectangle.info()
print(rectangle.info())
rectangle2 = Rectangle(11,7)
rectangle2.info()
print(rectangle2.info())
rectangle3 = Rectangle(6,2)
rectangle3.info()
print(rectangle3.info())

square = Square(5)
square.info()
print(square.info())
square2 = Square(10)
square2.info()
print(square2.info())
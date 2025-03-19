class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Point({self.x} , {self.y})'

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = point1 + point2

# result = point1 + point3
print(point3)
print(point1 == point2)

from abc import abstractmethod,ABC
# import sqlite3 (is a database in python )
class Logger(ABC):
    @abstractmethod
    def log(self, message,level):
        print(f"message: {message} level: {level}")

    @staticmethod
    def info(message,level):
        print(f"message: {message} level: {level}")

class DatBasedLogger(Logger):
    def log(self, message,level):
        print(f'Logging to Database. message: {message} level: {level}')
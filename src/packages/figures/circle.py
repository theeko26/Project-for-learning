import math


class Circle:
    def __init__(self, radius: float) -> None:
        """Инициализация окружности с заданным радиусом, в мм"""
        self.radius = radius
        
        #  Radius value validation (r > 0 only):
        if radius <= 0:
            raise ValueError("Radius must be positive only")
        self.radius = radius
    
    def area(self) -> float:
        """Вычисление площади окружности, в квадратных мм"""
        return math.pi * self.radius ** 2
    
    def circumference(self) -> float:
        """Вычисление длины окружности (периметра), в мм"""
        return 2 * math.pi * self.radius
    
    def diameter(self) -> float:
        """Вычисление диаметра окружности, в мм"""
        return 2 * self.radius
    
    def __str__(self) -> str:
        """Строковое представление окружности."""
        return f"Circle with radius: r = {self.radius} мм"
    
    def __repr__(self) -> str:
        """Формальное строковое представление для отладки."""
        return f"Circle({self.radius})"
    
    def __eq__(self, other) -> bool:
        """Сравнение окружностей по радиусу == (equals)"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius
    
    def __lt__(self, other) -> bool:
        """Сравнение окружностей по радиусу < (less than)"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius
    
    def __le__(self, other) -> bool:
        """Сравнение окружностей по радиусу <= (less than or equal)"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius <= other.radius
    
    def __gt__(self, other) -> bool:
        """Сравнение окружностей по радиусу > (greater than)"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius
    
    def __ge__(self, other):
        """Сравнение окружностей по радиусу >= (greater than or equal)"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius >= other.radius

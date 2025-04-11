import math


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        """Инициализация прямоугольника с заданными сторонами, в мм"""
        self.width = width
        self.height = height
        
        # Side values validation (both sides > 0):
        if width <= 0 or height <= 0:
            raise ValueError("Sides must be positive only")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Вычисление площади прямоугольника, в квадратных мм"""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Вычисление периметра прямоугольника, в мм"""
        return 2 * (self.width + self.height)
    
    def diagonal(self) -> float:
        """Вычисление диагонали прямоугольника, в мм"""
        return math.sqrt(self.width ** 2 + self.height ** 2)
    
    def max_side(self) -> float:
        """Возвращает наибольшую сторону прямоугольника"""
        return max(self.width, self.height)
    
    def __str__(self) -> str:
        """Строковое представление прямоугольника."""
        return f"Rectangle with sides: {self.width} мм × {self.height} мм"
    
    def __repr__(self) -> str:
        """Формальное строковое представление для отладки."""
        return f"Rectangle({self.width}, {self.height})"
    
    def __eq__(self, other) -> bool:
        """Сравнение прямоугольников по наибольшей стороне == (equals)"""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.max_side() == other.max_side()
    
    def __lt__(self, other) -> bool:
        """Сравнение прямоугольников по наибольшей стороне < (less than)"""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.max_side() < other.max_side()
    
    def __le__(self, other) -> bool:
        """
        Сравнение прямоугольников по наибольшей стороне <= (less than or equal)
        """
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.max_side() <= other.max_side()
    
    def __gt__(self, other) -> bool:
        """Сравнение прямоугольников по наибольшей стороне >
        (greater than)"""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.max_side() > other.max_side()
    
    def __ge__(self, other) -> bool:
        """Сравнение прямоугольников по наибольшей стороне >=
        (greater than or equal)"""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.max_side() >= other.max_side()

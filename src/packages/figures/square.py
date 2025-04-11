import math


class Square:
    def __init__(self, side: float) -> None:
        """Инициализация квадрата с заданной стороной, в мм"""
        self.side = side
        
        # Side value validation (a > 0 only):
        if side <= 0:
            raise ValueError("Side must be positive only")
        self.side = side
    
    def area(self) -> float:
        """Вычисление площади квадрата, в квадратных ммм"""
        return self.side ** 2
    
    def perimeter(self) -> float:
        """Вычисление периметра квадрата, в мм"""
        return 4 * self.side
    
    def diagonal(self) -> float:
        """Вычисление диагонали квадрата, в мм"""
        return self.side * math.sqrt(2)
    
    def __str__(self) -> str:
        """Строковое представление квадрата."""
        return f"Square with side: a = {self.side} мм"
    
    def __repr__(self) -> str:
        """Формальное строковое представление для отладки."""
        return f"Square({self.side})"
    
    def __eq__(self, other) -> bool:
        """Сравнение квадратов по стороне == (equals)"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.side == other.side
    
    def __lt__(self, other) -> bool:
        """Сравнение квадратов по стороне < (less than)"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.side < other.side
    
    def __le__(self, other) -> bool:
        """Сравнение квадратов по стороне <= (less than or equal)"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.side <= other.side
    
    def __gt__(self, other) -> bool:
        """Сравнение квадратов по стороне > (greater than)"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.side > other.side
    
    def __ge__(self, other) -> bool:
        """Сравнение квадратов по стороне >= (greater than or equal)"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.side >= other.side

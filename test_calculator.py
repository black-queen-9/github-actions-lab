# test_calculator.py
import pytest 
from calculator import Calculator  # Импортируем наш класс

# Создаем экземпляр калькулятора, который будем тестировать
calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5

def test_multiply():
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(7, 0) == 0

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3

# Тест на проверку ошибки (деление на ноль)
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Нельзя делить на ноль!"):
        calc.divide(5, 0)


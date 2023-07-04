# подключаем модуль для автотестов
import unittest
# импортируем функцию из другого файла
from hello_function import hello

# объявляем класс с тестом
class HelloTestCase(unittest.TestCase):
    # функция, которая проверит, как формируется приветствие
   def test_hello(self):
        # отправляем тестовую строку в функцию
        result = hello("миша")
        # задаём ожидаемый результат
        self.assertEqual(result, "Привет, Миша.")


# запускаем тестирование
if __name__ == '__main__':
    unittest.main() 
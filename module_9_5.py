class StepValueError(ValueError):
    """Пользовательское исключение для ошибки шага."""
    pass

class Iterator:
    """Итератор с заданными началом, концом и шагом."""

    def __init__(self, start, stop, step=1):
        """
        Инициализирует итератор.

        Args:
            start (int): Начальное значение итерации.
            stop (int): Конечное значение итерации.
            step (int, optional): Шаг итерации. По умолчанию 1.
        """
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        """Сбрасывает указатель и возвращает сам объект итератора."""
        self.pointer = self.start
        return self

    def __next__(self):
        """
        Возвращает следующее значение итерации.

        Raises:
            StopIteration: Если итерация достигла конца.
        """
        if self.step > 0 and self.pointer >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.pointer <= self.stop:
            raise StopIteration
        else:
            current = self.pointer
            self.pointer += self.step
            return current

# Пример использования
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

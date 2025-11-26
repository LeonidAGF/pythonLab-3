class my_stack:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    def __init__(self, obj=None):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.value = obj
        self.next = None
        self.minimum = obj

    def push(self, x: int) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        position = self

        if position == None or position.value == None:
            position.value = x
            position.minimum = x
        else:
            while position.next != None:
                if position.minimum > x:
                    position.minimum = x
                position = position.next
            position.next = my_stack(x)

    def pop(self) -> int:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        position = self

        if position == None or position.value == None:
            raise IndexError

        while position.next != None and position.next.next != None:
            position = position.next
        next_value: int = position.value
        if position.next != None and position.next.value != None:
            next_value = position.next.value
        if position.next == None:
            position.value = None
        position.next = None
        return next_value

    def peek(self) -> int:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        position = self

        if position == None or position.value == None:
            raise IndexError

        while position.next != None and position.next.next != None:
            position = position.next
        next_value: int = position.value
        if position.next != None and position.next.value != None:
            next_value = position.next.value
        return next_value

    # исключение при пустом
    def is_empty(self) -> bool:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if self == None or (self.next == None and self.value == None):
            return True
        else:
            return False

    def __len__(self) -> int:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        length = 0
        position = self
        if position != None and position.value != None:
            length += 1
        while position.next != None:
            length += 1
            position = position.next
        return length

    def min(self) -> int:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if self == None or self.value == None:
            raise IndexError
        return self.minimum

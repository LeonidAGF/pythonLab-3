class Object:
    """
    Класс, объект которого содержит какое-то значение и следующее значение в очереди
    """

    value = None
    next = None

    def __init__(self, obj):
        """
        Конструктор
        :return: Данная функция ничего не возвращает
        """
        self.value = obj
        self.next = None


class My_queue:
    """
    Класс реализующий очередь
    """

    head: Object = None
    tail: Object = None

    def __init__(self, obj):
        """
        Коонструктор
        :return: Данная функция ничего не возвращает
        """
        self.head = Object(obj)
        self.tail = self.head

    def enqueue(self, x: int) -> None:
        """
        Фуекция добаляет в конец очереди элемент x
        :return: Данная функция ничего не возвращает
        """
        if self.tail == None:
            raise IndexError

        is_new_object: int = 1
        if self.head is x:
            is_new_object = 0
        else:
            position: object = self.head
            if position.next != None:
                while position.next != None:
                    if position is x:
                        is_new_object = 0
                        break
                    position = position.next

        if not is_new_object:
            raise ValueError

        self.tail.next = Object(x)
        self.tail = self.tail.next

    def dequeue(self) -> int:
        """
        Функция удаляет первый элемент из очереди
        :return: Возвращает удалённый элемент
        """

        if self.head == None:
            raise IndexError
        n: int = self.head.value
        self.head = self.head.next
        if self.head == None:
            self.tail == None
        return n

    def front(self) -> int:
        """
        :return: Возвращает первый элемент очереди
        """
        if self.head == None:
            raise IndexError
        return self.head.value

    def is_empty(self) -> bool:
        """
        Функция проверяет очередь на пустоту
        :return: Возвращает True если очередь пуста, False иначе
        """
        if self.head == None:
            return True
        else:
            return False

    def __len__(self) -> int:
        """
        Функция считает количество элементов в очереди
        :return: Возвращает количесто элементов в очереди
        """
        length:int = 0
        if self.head != None:
            length += 1
        position: object = self.head
        if position.next != None:
            while position.next != None:
                length += 1
                position = position.next
        return length

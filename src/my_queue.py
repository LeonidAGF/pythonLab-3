class Object:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    value = None
    next = None

    def __init__(self, obj):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.value = obj
        self.next = None


class My_queue:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    head: Object = None
    tail: Object = None

    def __init__(self, obj):
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        self.head = Object(obj)
        self.tail = self.head

    def enqueue(self, x: int) -> None:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
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
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
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
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if self.head == None:
            raise IndexError
        return self.head.value

    def is_empty(self) -> bool:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        if self.head == None:
            return True
        else:
            return False

    def __len__(self) -> int:
        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
        length = 0
        if self.head != None:
            length += 1
        position: object = self.head
        if position.next != None:
            while position.next != None:
                length += 1
                position = position.next
        return length


"""    
class my_queue:
    
    def __init__(self, obj=None):
        
        self.value = obj
        self.next = None

    def enqueue(self, x: int) -> None:
        
        position = self
        if position.value==None:
            position.value = x
        else:
            while position.next != None:
                position = position.next
            position.next = my_queue(x)

    def dequeue(self):
        
        if self==None or self.value==None:
            raise IndexError

        n = self.value
        self.value = None
        if self != None:
            if(self.next!=None):
                self.value = self.next.value
                self.next = self.next.next
        return n

    def front(self) -> int:
        
        if self==None or self.value==None:
            raise IndexError
        return self.value

    def is_empty(self) -> bool:
        
        if self == None or (self.next==None and self.value==None):
            return True
        else:
            return False

    def __len__(self) -> int:

        length = 0
        position = self
        if position != None and position.value!=None:
            length+=1
        while position.next != None:
            length+=1
            position = position.next
        return length

"""

class Stack1:
    def __init__(self, obj=None):
        self.value = obj
        self.next = None
        self.minimum = obj

    def push(self, x: int) -> None:
        position = self
        while position.next != None:
            if position.minimum>x:
                position.minimum = x
            position = position.next
        position.next = Stack1(x)

    def pop(self) -> int:
        position = self
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
        position = self
        while position.next != None and position.next.next != None:
            position = position.next
        next_value: int = position.value
        if position.next != None and position.next.value != None:
            next_value = position.next.value
        return next_value

    # исключение при пустом
    def is_empty(self) -> bool:
        if self == None or (self.next == None and self.value == None):
            return True
        else:
            return False
    def __len__(self) -> int:
        length = 0
        position = self
        if position != None:
            length += 1
        while position.next != None:
            length += 1
            position = position.next
        return length
    def min(self) -> int:
        return self.minimum

class my_queue:
    def __init__(self, obj=None):
        self.value = obj
        self.next = None

    def enqueue(self, x: int) -> None:
        position = self
        while position.next != None:
            position = position.next
        position.next = my_queue(x)

    def dequeue(self):
        n = self.value
        self.value = None
        if self != None:
            if(self.next!=None):
                self.value = self.next.value
                self.next = self.next.next
        return n

    def front(self) -> int:
        return self.value

    def is_empty(self) -> bool:
        if self == None or (self.next==None and self.value==None):
            return True
        else:
            return False

    def __len__(self) -> int:
        length = 0
        position = self
        if position != None:
            length+=1
        while position.next != None:
            length+=1
            position = position.next
        return length

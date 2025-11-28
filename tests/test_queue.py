from src.my_queue import My_queue


def test_queue():
    """
        Тесты для my_queue
    """
    q = My_queue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert len(q) == 4
    assert q.front() == 1
    q.dequeue()
    assert len(q) == 3
    assert q.front() == 2
    assert q.is_empty() == False
    q.dequeue()
    q.dequeue()
    q.dequeue()
    assert q.is_empty() == True

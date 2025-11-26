from src.my_queue import My_queue
from src.my_stack import my_stack

def test_wrong_cases():
    """
        Тесты с ошибками
    """

    s = my_stack(1)
    s.pop()
    try:
        s.pop()
        assert 0==1
    except IndexError:
        assert 1==1
    try:
        s.peek()
        assert 0==1
    except IndexError:
        assert 1==1
    try:
        s.min()
        assert 0==1
    except IndexError:
        assert 1==1


    q = My_queue(1)
    try:
        q.enqueue(q.head)
        assert 0 == 1
    except ValueError:
        assert 1==1
    q.dequeue()
    try:
        q.dequeue()
        assert 0==1
    except IndexError:
        assert 1==1
    try:
        q.front()
        assert 0==1
    except IndexError:
        assert 1==1
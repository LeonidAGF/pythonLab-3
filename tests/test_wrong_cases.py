from src.my_queue import My_queue

def test_wrong_cases():
    """
        Тесты с ошибками
    """

    q:My_queue = My_queue(1)
    try:
        q.enqueue(q.head)
        assert 0 == 1
    except ValueError:
        assert 1 == 1
    q.dequeue()
    try:
        q.dequeue()
        assert 0 == 1
    except IndexError:
        assert 1 == 1
    try:
        q.front()
        assert 0 == 1
    except IndexError:
        assert 1 == 1

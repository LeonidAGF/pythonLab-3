from src.my_stack import my_stack



def test_stack():
    """
        Тесты my_stack
    """

    s = my_stack(1)
    s.push(2)
    s.push(3)
    s.push(4)
    assert len(s) == 4
    assert s.peek() == 4
    assert s.min() == 1
    s.pop()
    assert s.min() == 1
    assert len(s) == 3
    assert s.peek() == 3
    assert s.is_empty() == False
    s.pop()
    s.pop()
    s.pop()
    assert s.is_empty() == True
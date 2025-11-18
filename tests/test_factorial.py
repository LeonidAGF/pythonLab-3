from src.factorial import factorial, factorial_recursive


def test_factorial():
    """
        Тесты для factorial_recursive,factorial
    """
    assert factorial(0)==1
    assert factorial(1)==1
    assert factorial(6)==720
    assert factorial(20)==2432902008176640000
    assert factorial_recursive(6)==720
    assert factorial_recursive(1)==1
    assert factorial_recursive(0)==1
    assert factorial_recursive(20)==2432902008176640000
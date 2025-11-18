from src.fibo import fibo, fibo_recursive


def test_fibo():
    """
        Тесты для fibo,fibo_recursive
    """
    assert fibo(0)==0
    assert fibo(1)==1
    assert fibo(6)==8
    assert fibo(100)==354224848179261915075
    assert fibo_recursive(6)==8
    assert fibo_recursive(1)==1
    assert fibo_recursive(0)==0
    assert fibo_recursive(100)==354224848179261915075
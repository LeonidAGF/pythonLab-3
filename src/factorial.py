from functools import lru_cache


@lru_cache(maxsize=None)
def factorial_recursive(n: int) -> int:
    """
    Функция рекурсивно вычисляющая факториал
    :return: возвращает n!
    """
    if n == 1 or n == 0:
        return 1
    return factorial_recursive(n - 1) * n


def factorial(n: int) -> int:
    """
    Функция вычисляющая факториал при помощи цикла
    :return: возвращает n!
    """
    res: int = 1
    for i in range(2, n + 1):
        res *= i
    return res

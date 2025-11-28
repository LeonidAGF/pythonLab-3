import time


def timeit_once(func, *args, **kwargs) -> float:
    """
    Функция считает время пройденное с начала исполнения функции func
    :return: возвращает количество времени прошедшего с момента старта выполнения func и до её окончания
    """
    start_time:float = time.time()
    func(*args, **kwargs)
    return time.time() - start_time

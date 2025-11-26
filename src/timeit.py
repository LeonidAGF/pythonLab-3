import time

def timeit_once(func, *args, **kwargs) -> float:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    start_time = time.time()
    func(*args,**kwargs)
    return time.time() - start_time
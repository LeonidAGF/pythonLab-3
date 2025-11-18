import time

def timeit_once(func, *args, **kwargs) -> float:
    start_time = time.time()
    func(*args,**kwargs)
    return time.time() - start_time
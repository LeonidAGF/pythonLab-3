from functools import lru_cache

@lru_cache(maxsize=None)
def factorial_recursive(n:int) -> int:
    if n==1:
        return n
    return factorial_recursive(n-1)*n

def factorial_recursive(n:int) -> int:
    res:int = 1
    for i in range(2,n+1):
        res*=i
    return res
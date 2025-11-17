from functools import lru_cache

def fibo(n:int) -> int:
    fibonachi_list:list[int] = [0,1]
    for i in range(1,n):
        fibonachi_list.append(fibonachi_list[i]+fibonachi_list[i-1])
    return fibonachi_list[-1]

@lru_cache(maxsize=None)
def fibo_recursive(n:int) -> int:
   if n==0 or n==1:
       return n
   elif n>1:
       return fibo_recursive(n-1)+fibo_recursive(n-2)
   else:
       raise Exception
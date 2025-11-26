import math


def bucket_sort(a: list[float], buckets: int=None) -> list[float]:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    if len(a)==0:
        return a

    if a.count(a[0])==len(a):
        return a

    if buckets==None or buckets<2:
        buckets = max(a)-min(a)+1

    bucket_arr:list[[float]] = [[] for i in range(buckets)]

    arr:list[float] = a
    min_el:int = min(arr)
    ran:int = max(arr)-min(arr)+1

    bucket_num = 0
    i = math.ceil(min_el+ran/buckets)-1

    while bucket_num<len(bucket_arr):
        bucket_arr[bucket_num] = [int(el) for el in arr if el<=i and (el>i-math.ceil(ran/buckets) or bucket_num==0)]
        bucket_num+=1
        i+=math.ceil(ran/buckets)

    arr = []

    for j in bucket_arr:
        res = bucket_sort(j,2)
        if len(res)>0:
            arr+=(res)

    return arr

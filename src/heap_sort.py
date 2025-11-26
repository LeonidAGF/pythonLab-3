def heap_sort(a: list[int]) -> list[int]:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    arr: list[int] = a

    res: list[int] = []

    while len(arr) > 0:
        for i in range(len(arr) - 1, 0, -1):
            pos_origin: int = (i - 1) // 2
            if arr[pos_origin] > arr[i]:
                arr[pos_origin], arr[i] = arr[i], arr[pos_origin]
        res += [arr[0]]
        arr = arr[1:len(arr)]

    return res

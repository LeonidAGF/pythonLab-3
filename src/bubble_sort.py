def bubble_sort(a: list[int]) -> list[int]:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    unordered = 1
    len_a = len(a)
    while unordered:
        unordered = 0
        for i in range(0,len_a-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                unordered = 1
        len_a-=1
    return a
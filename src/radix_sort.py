def to_10_base(num: int, base: int) -> int:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    res: int = 0
    mnogitel: int = 1
    for i in range(len(str(num)) - 1, int('-' in str(num)) - 1, -1):
        res += int(str(num)[i]) * mnogitel
        mnogitel *= base
    return res


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    arr_plus: list[int] = [to_10_base(el, base) for el in a if el >= 0]
    arr_minus: list[int] = [to_10_base(el, base) for el in a if el < 0]

    if len(arr_minus) > 0:
        arr_minus = sort(arr_minus, 10)
        arr_plus = sort(arr_plus, 10)
        arr_minus = [-el for el in arr_minus]
        arr_minus.reverse()
        return arr_minus + arr_plus
    return sort(arr_plus, 10)


def sort(a: list[int], base: int = 10) -> list[int]:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    max_len: int = max([len(str(x)) for x in a])
    b: list[list[int]] = [[] for i in range(base)]

    for i in range(0, max_len):
        for el in a:
            digit: int = (el // (base ** i)) % base
            b[digit].append(el)
        a = [el for q in b for el in q]
        b = [[] for i in range(base)]

    return a

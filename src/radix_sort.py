def to_10_base(num: int, base: int) -> int:
    """
    Переводит число звписанное в системе счисления с основанием <10 в число в десятеричной системе счисления
    :return: Возвращает число переведённое из системы счисления с онованием <10 в десятиричную систему счисления
    """
    res: int = 0
    mnogitel: int = 1
    for i in range(len(str(num)) - 1, int('-' in str(num)) - 1, -1):
        res += int(str(num)[i]) * mnogitel
        mnogitel *= base
    return res


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Функция разделяющая массив чисел на 2 массива с положительными и отрицательными и использующая для каждого массива функцию sort, которая реализует поразрядную сортировку
    :return: Возвращает отсортированный по возрастанию массив чисел
    """

    arr_plus: list[int] = [to_10_base(el, base) for el in a if el >= 0]
    arr_minus: list[int] = [to_10_base(el, base) for el in a if el < 0]

    if len(arr_minus) > 0:
        arr_minus:list[int] = sort(arr_minus, 10)
        arr_plus:list[int] = sort(arr_plus, 10)
        arr_minus = [-el for el in arr_minus]
        arr_minus.reverse()
        return arr_minus + arr_plus
    return sort(arr_plus, 10)

def sort(a: list[int], base: int = 10) -> list[int]:
    """
    Функция реализующая поразрядную сортировку
    :return:  Возвращает отсортированный по возрастанию массив чисел
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

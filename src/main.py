from src.bubble_sort import bubble_sort
from src.constants import SAMPLE_CONSTANT
from src.counting_sort import counting_sort
from src.fibo import fibo, fibo_recursive
from src.heap_sort import heap_sort
from src.quick_sort import quick_sort
from src.radix_sort import radix_sort


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    lst = [8,2,5,3,3,4,1]
    print(heap_sort(lst))

if __name__ == "__main__":
    main()

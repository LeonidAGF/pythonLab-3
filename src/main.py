from src.banchmark import benchmark_sorts
from src.bubble_sort import bubble_sort
from src.bucket_sort import bucket_sort
from src.counting_sort import counting_sort
from src.heap_sort import heap_sort
from src.quick_sort import quick_sort
from src.radix_sort import radix_sort
from src.test_case_generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

arrays = {
    "rand_int_array": rand_int_array(500, 0, 1000, distinct=True),
    "many_duplicates": many_duplicates(100, 2),
    "nearly_sorted": nearly_sorted(100, 2),
    "reverse_sorted": reverse_sorted(500),
}

algos = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "heap_sort": heap_sort,
    "bucket_sort": bucket_sort,
    "counting_sort": counting_sort,
    "radix_sort": radix_sort,
}

d = benchmark_sorts(arrays, algos)

for func_name, link in d.items():
    print(func_name)
    print(link)

if __name__ == "__main__":
    main()

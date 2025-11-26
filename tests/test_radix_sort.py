from src.radix_sort import radix_sort
from src.test_case_generators import rand_int_array, reverse_sorted


def test_radix_sort():
    """
        Тесты для radix_sort
    """
    arr_test1:list[int] = rand_int_array(5,0,5,distinct=True,seed=555)
    arr_test1.sort()

    arr_test2:list[int] = rand_int_array(100,0,1000,seed=556)
    arr_test2.sort()

    arr_test3:list[int] = rand_int_array(250,800,1800,distinct=True,seed=557)
    arr_test3.sort()

    arr_test4:list[int] = rand_int_array(500,-1000,1000,distinct=True,seed=558)
    arr_test4.sort()

    arr_test5:list[int] = reverse_sorted(500)
    arr_test5_sorted:list[int] = arr_test5
    arr_test5_sorted.sort()

    assert radix_sort(rand_int_array(5,0,5,distinct=True,seed=555)) == arr_test1
    assert radix_sort(rand_int_array(100,0,1000,seed=556)) == arr_test2
    assert radix_sort(rand_int_array(250,800,1800,distinct=True,seed=557)) == arr_test3
    assert radix_sort(rand_int_array(500,-1000,1000,distinct=True,seed=558)) == arr_test4
    assert radix_sort(arr_test5) == arr_test5_sorted
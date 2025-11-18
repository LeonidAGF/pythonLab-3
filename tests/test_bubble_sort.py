from src.bubble_sort import bubble_sort
from src.test_case_generators import rand_int_array, reverse_sorted


def test_bubble_sort():
    """
        Тесты для bubble_sort
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

    assert bubble_sort(rand_int_array(5,0,5,distinct=True,seed=555)) == arr_test1
    assert bubble_sort(rand_int_array(100,0,1000,seed=556)) == arr_test2
    assert bubble_sort(rand_int_array(250,800,1800,distinct=True,seed=557)) == arr_test3
    assert bubble_sort(rand_int_array(500,-1000,1000,distinct=True,seed=558)) == arr_test4
    assert bubble_sort(arr_test5) == arr_test5_sorted
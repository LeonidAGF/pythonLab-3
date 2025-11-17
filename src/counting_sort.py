def counting_sort(a: list[int]) -> list[int] :
    min_el:int = min(a)
    max_el :int = max(a)
    count_list:list[int] = [0]*(max_el-min_el+1)
    for el in a:
        count_list[el - min_el] += 1
    a.clear()
    for pos in range(min_el,max_el+1):
        a += [pos] * count_list[pos-min_el]
    return a

def quick_sort(a: list[int]) -> list[int]:
    if len(a)>0:
        main_element:int = a[0]
        elements_bigger:list[int] = [int(el) for el in a if el>main_element]
        elements_lower:list[int] = [int(el) for el in a if el<main_element]
        elements_ecvivolent:list[int] = [main_element]*a.count(main_element)
        return quick_sort(elements_lower)+elements_ecvivolent+quick_sort(elements_bigger)
    return []
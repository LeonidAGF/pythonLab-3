from src.timeit import timeit_once


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    res: dict[str, dict[str, float]] = {}
    for func_name, link in algos.items():
        func_res:dict[str, float] = {}
        for data_name, data in arrays.items():
            func_res[data_name] = timeit_once(link,data)
        res[func_name] = func_res
    return res
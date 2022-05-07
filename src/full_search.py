from typing import Dict, List

from utils.calculate_func import stop_watch


@stop_watch
def full_search(target_list: List[int], target_value: int) -> bool:
    number_of_list = len(target_list)
    def __solve(i: int, m: int) -> bool:
        if (m == 0):
            return True
        if (i >= number_of_list):
            return False
        return __solve(i+1, m) or __solve(i+1, m - target_list[i]) 
    return __solve(0, target_value)


def main():
    target_list = [1, 5, 7]
    print("target_value: {} -> {}".format(8, full_search(target_list, 8)))
    print("target_value: {} -> {}".format(6, full_search(target_list, 6)))
    print("target_value: {} -> {}".format(9, full_search(target_list, 9)))


if __name__ == '__main__':
    main()
import random
from typing import Dict, List

from utils.calculate_func import stop_watch


@stop_watch
def linear_search(target_list: List[int], key: int) -> bool:
    for i in range(len(target_list)):
        if (target_list[i] == key):
            return True
    return False
        
@stop_watch
def linear_search_2(target_list: List[int], key: int) -> bool:
    target_list.append(key)
    i = 0
    while(target_list[i] != key):
        i += 1
    return len(target_list)-1 != i

@stop_watch
def bynary_search(target_list: List[int], key: int) -> bool:
    left = 0
    right = len(target_list)
    while left < right:
        center = (left + right) // 2
        if target_list[center] == key:
            return True
        if key < target_list[center]:
            right = center
        else:
            left = center+1
    return False

@stop_watch
def hash_search(target_hash: Dict[int, List[int]], key: int) -> bool:
    def __linear_search_2(target_list: List[int], key: int) -> bool:
        target_list.append(key)
        i = 0
        while(target_list[i] != key):
            i += 1
        return len(target_list)-1 != i

    hash_value = caluculate_hash(key)
    target_list = target_hash[hash_value]
    return __linear_search_2(target_list, key)


def caluculate_hash(target_value: int) -> int:
    hash_value = 269
    return target_value % hash_value

def main():
    key = 657
    target_list = [random.randint(1, 1000) for i in range(10000000)]
    target_list.append(key)
    random.shuffle(target_list)

    target_linear = target_list

    target_bynary = sorted(target_linear)

    target_hash = {}
    for value in target_linear:
        hash_value = caluculate_hash(value)
        if hash_value in target_hash.keys():
            target_hash[hash_value].append(value)
        else:
            target_hash[hash_value] = [value]
        
    print('start!')

    print(linear_search(target_linear, key))
    print(linear_search_2(target_linear, key))
    print(bynary_search(target_bynary, key))
    print(hash_search(target_hash, key))


if __name__ == '__main__':
    main()

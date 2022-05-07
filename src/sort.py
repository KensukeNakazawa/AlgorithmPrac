from typing import List

from utils.calculate_func import stop_watch


@stop_watch
def merge_sort(target_list: List[int]) -> List[int]:
    def __merge_sort(_target_list: List[int]):
        if len(_target_list) <= 1:
            return _target_list

        center = len(_target_list) // 2
        left, right = _target_list[:center], _target_list[center:]
        left = __merge_sort(left)
        right = __merge_sort(right)
        return __merge(left, right)

    def __merge(left_list: List[int], right_list: List[int]):
        merged_list = []
        i = j = 0
        print('merge target(left): ', left_list)
        print('merge target(right): ', right_list)

        length_left, length_right = len(left_list), len(right_list)
        print('merge')
        while i < length_left and j < length_right:
            print(merged_list)
            if left_list[i] <= right_list[j]:
                merged_list.append(left_list[i])
                i += 1
            else:
                merged_list.append(right_list[j])
                j += 1
        
        if i < length_left:
            merged_list.extend(left_list[i:])
        if j < length_right:
            merged_list.extend(right_list[j:])
        return merged_list

    return __merge_sort(target_list)


def main():
    target_list = [9, 6, 7, 2, 5, 1, 8, 4, 2]
    print(merge_sort(target_list))


if __name__ == '__main__':
    main()
    
def _sort(_list):

    length = len(_list) - 1
    print(length)
    i = 0
    while(length > i):
        j = i + 1
        while(length > j):
            if(_list[i] > _list[j]):
                _list[i] , _list[j] = _list[j] , _list[i]

            j += 1

        i += 1
    return _list
        


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return _sort(list1 + list2)

# print(shadow_merge([1, 3, 5], [2, 4, 6]))

print(shadow_merge([1, 3, 5], [2, 4, 6]))
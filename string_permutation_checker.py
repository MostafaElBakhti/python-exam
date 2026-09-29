# def string_permutation_checker(s1: str, s2: str) -> bool:
#     return(sorted(s1) == sorted(s2))


def string_permutation_checker(s1: str, s2: str) -> bool:

    if len(s1) != len(s2):
        return False

    count = {
        char : 0
        for char in s1
    }

    for char in s1:
        count[char] += 1

    for char in s2:
        if char not in count :
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True    


print(string_permutation_checker("aabcc", "bca ac"))
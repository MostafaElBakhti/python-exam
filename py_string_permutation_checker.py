def string_permutation_checker(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    return sorted(s1) == sorted(s2)
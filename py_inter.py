def inter(s1: str, s2: str) -> str:
    khawi = ""
    
    for x in s1:
        if x in s2 and x not in khawi:
            khawi += x
    return khawi


print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))
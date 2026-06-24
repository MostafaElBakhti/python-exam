def inter(s1: str, s2: str) -> str:
    text = ""

    for char in s1:
        if char in s2 and char not in text:
            text += char 

    return text


print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))
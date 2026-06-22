def inter(s1: str, s2: str) -> str:

    text = ""
    for x in s1:
        if x in s2 and x not in text:
            text += x

    return text


# def inter(s1: str, s2: str) -> str:

#     text = ""

#     for x in s1:
#         # print(f"s1 :{x}")
#         for y in s2: 
#             # print(y)
#             if x == y:
#                 already = 1
#                 for k in text:
#                     if x == k:
#                         already = 0
#                 if already == 1:
#                     text += x
#                 break
#     return text


print(inter("hello", "world"))
print(inter("banana", "band"))
print(inter("abcabc", "bc"))
print(inter("abc", "xyz"))
print(inter("", "abc"))
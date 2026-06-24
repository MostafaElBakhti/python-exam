def hidenp(small: str, big: str) -> bool:

    i = 0

    for char in big:
        if i < len(small) and char == small[i]:
            i += 1
    return i == len(small)



    # for x in small:
    #     # print(f"s1 :{x}")
    #     for y in big: 
    #         # print(y)
    #         found = 0
    #         if x == y:
    #             found = 1
    #             break
    #     if found == 0:
    #         return False
    # return True
# hidenp("abc", "a1b2c3")

print(hidenp("aec", "abcde"))



# Input
# hidenp("abc", "a1b2c3")
# Output
# True


# Input
# hidenp("ace", "abcde")
# Output
# True


# Input
# hidenp("aec", "abcde")
# Output
# False
def hidenp(small: str, big: str) -> bool:

    i = 0 
    for c in big:
        if i < len(small) and c == small[i]:
            i += 1

    return i == len(small)


print(hidenp("abc", "a1b2c3"))
print(hidenp("aec", "abcde"))
print(hidenp("sing","subsequence testing"))



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
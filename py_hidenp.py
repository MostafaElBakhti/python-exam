def hidenp(small: str, big: str) -> bool:
    for x in small:
        # print(f"s1 :{x}")
        for y in big: 
            # print(y)
            found = 0
            if x == y:
                found = 1
                break
        if found == 0:
            return False
    return True

print(hidenp("abc", "a1b2c3"))
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
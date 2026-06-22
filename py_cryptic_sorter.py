def cryptic_sorter(strings: list[str]) -> list[str]:

    
    return sorted(strings, key=(len, ))


print(cryptic_sorter(["apple", "banana", "kiwi", "cherry", "aab","aaa", "aac", "a", "B"]))


# c = ["apple", "banana", "kiwi", "cherry", "aa"]
# c.sort(key=len)
# print(c)

# d = [(1, 3), (2, 2), (3, 1),(2,0)]
# d.sort(key=lambda x: x[1])
# print(d)
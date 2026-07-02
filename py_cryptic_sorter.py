def count_vo(s : str):
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1
    return count

def cryptic_sorter(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda x: (len(x), x.lower(), count_vo(x)))


print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
def count_vowels(text: str):
    vowels = ("aeiou")
    count = 0 
    for x in text:
        if x in vowels:
            count += 1
    return count


def cryptic_sorter(strings: list[str]) -> list[str]:

    
    return sorted(strings, key=lambda x: (len(x), x.lower(),x , count_vowels(x)) )


print(cryptic_sorter(["aaa","bbb","AAA","BBB"])) 
# Output
# ["AAA", "aaa", "BBB", "bbb"

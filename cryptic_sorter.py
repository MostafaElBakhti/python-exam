def count_vowels(s1):
    count = 0 
    for char in s1:
        if char.lower() in "aeiou":
            count += 1

    return count 


def cryptic_sorter(strings: list[str]) -> list[str]:

    strings = strings.copy()

    i = 0 
    while ( i < len(strings) - 1):
        j = i + 1
        while( j < len(strings) ):

            if len(strings[i]) > len(strings[j]):
                strings[i], strings[j] = strings[j], strings[i]

            elif len(strings[i]) == len(strings[j]):
                if strings[i].lower() > strings[j].lower():
                    strings[i], strings[j] = strings[j], strings[i]

                elif strings[i].lower() == strings[j].lower():
                    if count_vowels(strings[i]) > count_vowels(strings[j]):
                        strings[i], strings[j] = strings[j], strings[i]
            
            j += 1
        i += 1
    return(strings)



print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
print(cryptic_sorter(["hello","world","hi","test"]))
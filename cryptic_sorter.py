def count_vowels(s1):
    count = 0 
    for char in s1:
        if char in "aeiou":
            count += 1

    return count 


def cryptic_sorter(strings: list[str]) -> list[str]:
    
    print(len(strings))
    i = 0 
    while ( i < len(strings) - 1):
        j = i + 1
        while( j < len(strings) ):
            if len(strings[i]) > len(strings[j]):
                tmp = strings[i]
                strings[i] = strings[j]
                strings[j] = tmp
            elif len(strings[i]) == len(strings[j]):
                if strings[i].lower() > strings[j].lower():
                    tmp = strings[i]
                    strings[i] = strings[j]
                    strings[j] = tmp
                else:
                    print("equal")
            
            j += 1
        i += 1
    print(strings)



print(cryptic_sorter(["apple","Cat","banana","dog","elephant","act"]))
print(cryptic_sorter(["aaa","bbb","aAA","BBB"]))
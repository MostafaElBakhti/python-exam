# def count_vowels(s1):
#     count = 0 
#     for char in s1:
#         if char.lower() in "aeiou":
#             count += 1
#     return count 


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

                # elif strings[i].lower() == strings[j].lower():
                #     strings[i], strings[j] = strings[j], strings[i]
            
            j += 1
        i += 1
    return(strings)


def cryptic_sorter(strings: list[str]) -> list[str]:
    key = lambda s: (len(s) , s.lower() , sum(c.lower() in "aeiou" for c in s))
    idx = list(range(len(strings)))
    for i in range(1, len(idx)):
        j = i
        while j > 0 and key(strings[idx[j - 1]]) > key(strings[idx[j]]):
            idx[j-1] , idx[j] = idx[j] , idx[j - 1]
            j -= 1
    return [strings[i] for i in idx]


print(cryptic_sorter(["CAR","car"]))
# print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
# print(cryptic_sorter(["hello","world","hi","test"]))
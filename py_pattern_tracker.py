def pattern_tracker(text: str) -> int:
    count = 0
    i = 0
    while i < len(text) - 1:
        if text[i].isdigit() and text[i+1].isdigit():
            if (int(text[i+1] )- int(text[i])) == 1:
                count += 1
        i += 1
    return count


print(pattern_tracker(""))                  # 0
print(pattern_tracker("a"))                 # 0
print(pattern_tracker("1"))                 # 0

print(pattern_tracker("12"))                # 1
print(pattern_tracker("23"))                # 1
print(pattern_tracker("89"))                # 1
print(pattern_tracker("90"))                # 0

print(pattern_tracker("123"))               # 2
print(pattern_tracker("1234"))              # 3
print(pattern_tracker("01234567"))          # 7

print(pattern_tracker("987654321"))         # 0
print(pattern_tracker("97531"))             # 0

print(pattern_tracker("12a34"))             # 2
print(pattern_tracker("127a345"))           # 3
print(pattern_tracker("1a2b3c4"))           # 0

print(pattern_tracker("ab12cd23"))          # 2
print(pattern_tracker("ab123cd"))           # 2

print(pattern_tracker("111111"))            # 0
print(pattern_tracker("222233"))            # 1

print(pattern_tracker("0123401234"))        # 8
print(pattern_tracker("123456789"))         # 8

print(pattern_tracker("789"))               # 2
print(pattern_tracker("6789"))              # 3

print(pattern_tracker("001122334455"))      # 5

print(pattern_tracker("a1b2c3d4e5"))        # 0
print(pattern_tracker("a12b23c34"))         # 3

print(pattern_tracker("12!23@34#45"))       # 4

print(pattern_tracker("999999"))            # 0
print(pattern_tracker("000000"))            # 0

print(pattern_tracker("1234567890"))        # 8
print(pattern_tracker("0123456789"))        # 9

print(pattern_tracker("01"))                # 1
print(pattern_tracker("09"))                # 0
print(pattern_tracker("10"))                # 0
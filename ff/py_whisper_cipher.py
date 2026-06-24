
def Shift_alphabet(alphabet, i):
    result = ""
    for char in alphabet:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + i) % 26 + ord("a"))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + i) % 26 + ord("A"))
        else:
            result += char

    return (result)

# ord() char to num
# chr() num to char

print(Shift_alphabet("abz", 1))
# "bca"

print(Shift_alphabet("AbZ", 1))
# "BcA"

# With spaces and punctuation
print(Shift_alphabet("Hello World!", 3))
# "Khoor Zruog!"

# Negative shift
print(Shift_alphabet("bca", -1))
# "abz"

# Large shift (wrap around)
print(Shift_alphabet("abc", 26))
# "abc"

print(Shift_alphabet("xyz", 3))
# "abc"

# Mixed characters
print(Shift_alphabet("Python 3.8!", 5))
# "Udymts 3.8!"

# Edge cases
print(Shift_alphabet("", 10))
# ""

print(Shift_alphabet("12345", 4))
# "12345"
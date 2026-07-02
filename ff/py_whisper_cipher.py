
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



def whisper_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if  "a" <= char  <= "z":
            result +=  chr( (ord(char) - ord('a') + shift) % 26  + ord('a'))
        elif "A" <= char  <= "Z":
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char 

    return result


def whisper_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if  "a" <= char  <= "z":
            result += chr( (ord(char) - ord('a') + shift)  % 26 + ord('a') )
        elif  "A" <= char  <= "Z":
            result += chr( (ord(char) - ord('A') + shift)  % 26 + ord('A') )
        else:
            result += char

    return result





def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    
    try:
        decimal = int(number, from_base)
    except ValueError:
        return "ERROR"
    
    if to_base == 10 :
        return str(decimal)
    
    result = ""
    while decimal:
        result = digits[decimal % to_base] + result
        decimal //= to_base

    return result or "0"
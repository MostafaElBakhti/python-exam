
# def Shift_alphabet(alphabet, i):
#     result = ""
#     for char in alphabet:
#         if 'a' <= char <= 'z':
#             result += chr((ord(char) - ord('a') + i) % 26 + ord("a"))
#         elif 'A' <= char <= 'Z':
#             result += chr((ord(char) - ord('A') + i) % 26 + ord("A"))
#         else:
#             result += char

#     return (result)



def whisper_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text :
        if 'a' <= char <= 'z':
            result += chr( (ord(char) - ord('a') + shift ) % 26 + ord('a') )
        elif 'A' <= char <= 'Z':
            result += chr( (ord(char) - ord('A') + shift ) % 26 + ord('A') )
        else :
            result += char

    return result




print(whisper_cipher("hello", 3))
print(whisper_cipher("Hello World!", 1))
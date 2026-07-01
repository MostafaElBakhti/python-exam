def string_sculptor(text: str) -> str:
    upper = True
    result = ""

    for char in text:
        if char.isalpha():    
            if upper:
                result += char.lower()
            else:
                result += char.upper()
            upper = not upper
        else:
            result += char
    return result
            
print(string_sculptor("HELLO"))
def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    try:
        decimal = int(number, from_base)
    except ValueError:
        return "ERROR"

    if to_base == 10:
        return str(decimal)

    result = ""
    while decimal:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return result or "0"

number_base_converter("1010", 2, 10)
number_base_converter("255", 10, 16)

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    
    try:
        decimal = int(number, from_base)
    except ValueError:
        return "ERROR"

    if to_base == 10:
        return str(decimal)
    
    result = ""
    while decimal:
        result = digits[decimal % to_base] + result
        decimal //= to_base

    return result or "0"



def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36) or not number:
        return "ERROR"
    value = 0
    for ch in number.upper():
        if ch not in digits[:from_base]:
            return "ERROR"
        value = value * from_base + digits.index(ch)
    if value == 0:
        return "0"
    result = ""
    while value:
        result = digits[value % to_base] + result
        value //= to_base
    return result
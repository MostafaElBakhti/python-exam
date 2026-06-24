def string_sculptor(text: str) -> str:
    txt = ""
    upper = True
    for char in text:
        if upper:
            txt += char.upper()
        else:
            txt += char.lower()
        upper = not upper

    return txt

print(string_sculptor("hello"))
# Output
# "hElLo"


def string_sculptor(text: str) -> str:
    mytext = ""

    for char in text :
        if char.isalpha():
            mytext += char
    
    final_text = ""
    flag = 0
    for char in mytext:
        if flag == 0:
            final_text += char.lower()
            flag = 1
        else:
            final_text += char.upper()
            flag = 0

    return final_text


print(string_sculptor("he12llo"))
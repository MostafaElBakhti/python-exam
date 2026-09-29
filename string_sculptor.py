def string_sculptor(text: str) -> str:

    res = ""
    flag = 1

    for char in text:
        if char.isalpha():
            if flag == 1:
                res += char.lower()
                flag = 0
            else:
                res += char.upper()
                flag = 1
        else:
            res += char 
            if char == " ":
                flag = 1
    
    return res





print(string_sculptor("aBc123def"))
print(string_sculptor("Hello World"))
# Output
# "pYtHoN3.9!"
# Output
# "hElLo wOrLd"
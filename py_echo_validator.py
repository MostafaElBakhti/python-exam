def echo_validator(text: str) -> bool:
    cleaned = ""
    for char in text.lower():
        if char.isalpha():
            cleaned += char

    if cleaned == "":
        return False
    # else:
    return cleaned == cleaned[::-1]




print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator(""))
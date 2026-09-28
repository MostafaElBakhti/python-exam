def echo_validator(text: str) -> bool:
    test = "".join(char.lower() for char in text if char.isalpha() )
    return test == test[::-1]


print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("Was it a car or a cat I saw"))
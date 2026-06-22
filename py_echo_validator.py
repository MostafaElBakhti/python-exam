def echo_validator(text: str) -> bool:
    cleaned = " "
    for char in text:
        if char.islpha():
            cleaned += char



# echo_validator("A man a plan a canal Panama")

def bracket_validator(s: str) -> bool:
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


print(bracket_validator("()"))                # True
print(bracket_validator("()[]{}"))            # True
print(bracket_validator("(]"))                # False
print(bracket_validator("([)]"))              # False
print(bracket_validator("{[]}"))              # True
print(bracket_validator("hello(world)"))      # True
print(bracket_validator("((())"))             # False
print(bracket_validator(""))                  # True
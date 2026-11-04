def bracket_validator(s: str) -> bool:
    queue: list = ["1"]
    for x in s:
        if x == "(" or x == "[" or x == "{":
            queue.append(x)
        elif queue[-1] == "(" and x == ")":
            queue.pop()
        elif queue[-1] == "[" and x == "]":
            queue.pop()
        elif queue[-1] == "{" and x == "}":
            queue.pop()
        elif x == ")" or x == "]" or x == "}":
            queue.append(x)
    return queue == ["1"]


print(bracket_validator("()"))
print(bracket_validator("()[]{}"))
print(bracket_validator("(]"))
print(bracket_validator("([)]"))
print(bracket_validator("{[]}"))
print(bracket_validator("hello(world)"))
print(bracket_validator("((())"))
print(bracket_validator(""))

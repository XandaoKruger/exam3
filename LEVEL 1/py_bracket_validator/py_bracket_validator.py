def bracket_validator(s: str) -> bool:

    fila: list = ["1"]

    for x in s:
        if x == "(" or x == "[" or x == "{":
            fila.append(x)
        elif fila[-1] == "(" and x == ")":
            fila.pop()
        elif fila[-1] == "[" and x == "]":
            fila.pop()
        elif fila[-1] == "{" and x == "}":
            fila.pop()
        elif x == "(" or x == "[" or x == "{":
            fila.append(x)
    return fila == ["1"]

print(bracket_validator("()"))
print(bracket_validator("()[]{}"))
print(bracket_validator("(]"))
print(bracket_validator("([)]"))
print(bracket_validator("{[]}"))
print(bracket_validator("hello(world)"))
print(bracket_validator("((())"))
print(bracket_validator(""))
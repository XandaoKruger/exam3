def string_sculptor(text: str) -> str:
    lowered: bool = False
    copy: str = ""
    for i in range(0, len(text)):
        if text[i] == " ":
            copy += text[i]
            lowered = False
        elif text[i].isalpha() and not lowered:
            copy += text[i].lower()
            lowered = True
        elif text[i].isalpha() and lowered:
            copy += text[i].upper()
            lowered = False
        else:
            copy += text[i]
    return copy


print(string_sculptor("hello"))
print(string_sculptor("Hello World"))
print(string_sculptor("abc123def"))
print(string_sculptor("Python3.9!"))
print(string_sculptor(""))

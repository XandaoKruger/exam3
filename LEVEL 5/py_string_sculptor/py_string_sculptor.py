def string_sculptor(text: str) -> str:

    lowered: bool = False
    copy: str = ""

    for c in range(0, len(text)):

        if text[c] == " ":
            copy += text[c]
            lowered = False
        elif text[c].isalpha() and not lowered:
            copy += text[c].lower()
            lowered = True
        elif text[c].isalpha() and lowered:
            copy += text[c].upper()
            lowered = False
        else:
            copy += text[c]
    return copy


print(string_sculptor("hello"))
print(string_sculptor("Hello World"))
print(string_sculptor("abc123def"))
print(string_sculptor("Python3.9!"))
print(string_sculptor(""))

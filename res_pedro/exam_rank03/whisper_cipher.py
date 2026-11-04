def whisper_cipher(text: str, shift: int) -> str:
    res: str = ""
    s1: str = "abcdefghijklmnopqrstuvwxyz"
    s2: str = "abcdefghijklmnopqrstuvwxyz".upper()
    r: int = 0
    for c in range(0, len(text)):
        if text[c] in s1:
            r = s1.find(text[c])
            res += s1[(r + shift) % 26]
        elif text[c] in s2:
            r = s2.find(text[c])
            res += s2[(r + shift) % 26]
        else:
            res += text[c]
    return res


print(whisper_cipher("hello", 3))
print(whisper_cipher("Hello World!", 1))
print(whisper_cipher("xyz", 3))
print(whisper_cipher("ABC123def", 5))
print(whisper_cipher("", 10))
print(whisper_cipher("abc", -3))
